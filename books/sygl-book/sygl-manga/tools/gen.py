#!/usr/bin/env python3
"""
Sygl Manga — RunPod ComfyUI+FLUX generator (account-agnostic).

Works with ANY RunPod serverless ComfyUI+FLUX endpoint. No secrets live in this
repo — you pass your endpoint id + API key via environment variables:

    export RUNPOD_ENDPOINT_ID=xxxxxxxxxxxx      # from your endpoint's page
    export RUNPOD_API_KEY=rpa_...               # RunPod → Settings → API Keys

Endpoint requirement: deploy from the RunPod Hub -> "ComfyUI" **release 5.8.5**
(the 5.8.6 FLUX.1-dev build crash-loops). 24 GB GPU, Active workers 0, Max 1.
The model checkpoint name it ships with is `flux1-dev-fp8.safetensors` (change
CKPT below if your endpoint differs — a wrong name FAILS with a list of valid ones).

USAGE
  # text -> image (one or more prompts, each its own seed)
  python gen.py txt2img --prompt "PROMPT" --out out.png [--seed 42] [--w 1216 --h 832]

  # inpaint a stump (or anything) over a region of an existing image
  python gen.py inpaint --base in.png --out out.png \
      --ellipse 808 596 930 690 \
      --prompt "left forearm ends in a smooth rounded stump, no hand, no fingers"

  # health check
  python gen.py health

See README.md (VISUAL STYLE, working config) and chapter-01-storyboard.md for the
canon rules every prompt must respect (Bal stump/no-sygl, spot-color sygls, geography).
"""
import os, sys, json, time, base64, argparse, urllib.request, urllib.error

CKPT = "flux1-dev-fp8.safetensors"
STYLE = ("manga, monochrome, greyscale, screentone, clean ink lineart, shonen manga, "
         "high detail")

def _env():
    e = os.environ.get("RUNPOD_ENDPOINT_ID"); k = os.environ.get("RUNPOD_API_KEY")
    if not e or not k:
        sys.exit("Set RUNPOD_ENDPOINT_ID and RUNPOD_API_KEY env vars first.")
    return e, k

def _req(url, data=None):
    e, k = _env()
    hdr = {"Authorization": f"Bearer {k}"}
    if data is not None:
        hdr["Content-Type"] = "application/json"; data = json.dumps(data).encode()
    for attempt in range(5):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(url, data=data, headers=hdr), timeout=120))
        except urllib.error.HTTPError as ex:
            print("HTTP", ex.code, ex.read().decode()[:500]); raise
        except Exception as ex:
            if attempt == 4: raise
            time.sleep(2 * (attempt + 1))

def _base(): e, _ = _env(); return f"https://api.runpod.ai/v2/{e}"

def health():
    print(json.dumps(_req(f"{_base()}/health"), indent=2))

def _run_and_wait(payload, out):
    jid = _req(f"{_base()}/run", payload).get("id")
    print("job", jid, "...", flush=True)
    for _ in range(120):
        r = _req(f"{_base()}/status/{jid}")
        st = r.get("status")
        if st == "COMPLETED":
            imgs = (r.get("output") or {}).get("images", [])
            for im in imgs:
                d = im.get("data") or im.get("image")
                if d:
                    open(out, "wb").write(base64.b64decode(d)); print("SAVED", out); return True
            print("NO IMAGE:", json.dumps(r.get("output"))[:800]); return False
        if st == "FAILED":
            print("FAILED:", json.dumps(r)[:800]); return False
        time.sleep(5)
    print("timeout"); return False

def _txt2img_wf(prompt, neg, seed, w, h):
    return {
        "4": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["4", 1]}},
        "7": {"class_type": "CLIPTextEncode", "inputs": {"text": neg, "clip": ["4", 1]}},
        "5": {"class_type": "EmptySD3LatentImage", "inputs": {"width": w, "height": h, "batch_size": 1}},
        "3": {"class_type": "KSampler", "inputs": {"seed": seed, "steps": 24, "cfg": 1.0,
              "sampler_name": "euler", "scheduler": "simple", "denoise": 1.0,
              "model": ["4", 0], "positive": ["6", 0], "negative": ["7", 0], "latent_image": ["5", 0]}},
        "8": {"class_type": "VAEDecode", "inputs": {"samples": ["3", 0], "vae": ["4", 2]}},
        "9": {"class_type": "SaveImage", "inputs": {"filename_prefix": "gen", "images": ["8", 0]}},
    }

def txt2img(a):
    prompt = a.prompt if a.raw else f"{a.prompt}, {STYLE}"
    wf = _txt2img_wf(prompt, a.neg, a.seed, a.w, a.h)
    _run_and_wait({"input": {"workflow": wf}}, a.out)

def inpaint(a):
    # build a black mask with a white ellipse over the region to regenerate
    from PIL import Image, ImageDraw
    im = Image.open(a.base); W, H = im.size
    m = Image.new("RGB", (W, H), (0, 0, 0))
    ImageDraw.Draw(m).ellipse(tuple(a.ellipse), fill=(255, 255, 255))
    b = base64.b64encode(open(a.base, "rb").read()).decode()
    import io; buf = io.BytesIO(); m.save(buf, "PNG")
    mb = base64.b64encode(buf.getvalue()).decode()
    prompt = a.prompt if a.raw else f"{a.prompt}, {STYLE}"
    wf = {
        "10": {"class_type": "LoadImage", "inputs": {"image": "base.png"}},
        "11": {"class_type": "LoadImage", "inputs": {"image": "mask.png"}},
        "12": {"class_type": "ImageToMask", "inputs": {"image": ["11", 0], "channel": "red"}},
        "4": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["4", 1]}},
        "7": {"class_type": "CLIPTextEncode", "inputs": {"text": a.neg, "clip": ["4", 1]}},
        "13": {"class_type": "VAEEncodeForInpaint", "inputs": {"pixels": ["10", 0], "vae": ["4", 2],
               "mask": ["12", 0], "grow_mask_by": a.grow}},
        "3": {"class_type": "KSampler", "inputs": {"seed": a.seed, "steps": 26, "cfg": 1.0,
              "sampler_name": "euler", "scheduler": "simple", "denoise": 1.0,
              "model": ["4", 0], "positive": ["6", 0], "negative": ["7", 0], "latent_image": ["13", 0]}},
        "8": {"class_type": "VAEDecode", "inputs": {"samples": ["3", 0], "vae": ["4", 2]}},
        "9": {"class_type": "SaveImage", "inputs": {"filename_prefix": "inp", "images": ["8", 0]}},
    }
    payload = {"input": {"workflow": wf, "images": [
        {"name": "base.png", "image": b}, {"name": "mask.png", "image": mb}]}}
    _run_and_wait(payload, a.out)

def main():
    ap = argparse.ArgumentParser(description="Sygl manga RunPod FLUX generator")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("health")
    t = sub.add_parser("txt2img")
    t.add_argument("--prompt", required=True); t.add_argument("--out", required=True)
    t.add_argument("--neg", default="color, watermark, signature, text, border, deformed")
    t.add_argument("--seed", type=int, default=42)
    t.add_argument("--w", type=int, default=1216); t.add_argument("--h", type=int, default=832)
    t.add_argument("--raw", action="store_true", help="use --prompt verbatim (don't append STYLE)")
    t.set_defaults(func=txt2img)
    p = sub.add_parser("inpaint")
    p.add_argument("--base", required=True); p.add_argument("--out", required=True)
    p.add_argument("--prompt", required=True)
    p.add_argument("--ellipse", nargs=4, type=int, required=True, metavar=("x0", "y0", "x1", "y1"))
    p.add_argument("--neg", default="hand, fingers, palm, fist, smudge, deformed")
    p.add_argument("--grow", type=int, default=8); p.add_argument("--seed", type=int, default=7)
    p.add_argument("--raw", action="store_true")
    p.set_defaults(func=inpaint)
    a = ap.parse_args()
    if a.cmd == "health": health()
    else: a.func(a)

if __name__ == "__main__":
    main()
