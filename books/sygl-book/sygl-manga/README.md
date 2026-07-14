# Sygl Manga

Manga adaptation of **Sygl**. Everything for the illustrated version lives in
this folder; the prose book stays in the parent `books/sygl-book/`.

## Folder contents
- `README.md` — this file: RunPod + ComfyUI setup, working config, workflow.
- `bal-manga.png` — early Pollinations style test (free, keyless).
- `panel-familiar-reveal.jpg` — Pollinations test panel (familiar-class reveal).
- `panel-bal-flux.png` — first WORKING FLUX panel via the RunPod API (Bal).

## ▶ RUN IMAGE GENERATION (any RunPod account — e.g. a different one)
Everything needed is in `tools/gen.py`. No API key is stored in this repo.

1. **Deploy the endpoint** on the account you want to use: RunPod → Serverless →
   New Endpoint → **Deploy from the Hub → "ComfyUI" release 5.8.5** (NOT 5.8.6 — it
   crash-loops). GPU 24 GB · Active workers 0 · Max 1 · FlashBoot on. No env vars needed
   on the endpoint (the 5.8.5 build has the FLUX model baked in — non-gated).
2. **Get two values:** the **Endpoint ID** (on the endpoint page / in the `/v2/<ID>/run`
   URL) and an **API key** (RunPod → Settings → API Keys → Create).
3. **Set them as env vars and run:**
   ```bash
   export RUNPOD_ENDPOINT_ID=your_endpoint_id
   export RUNPOD_API_KEY=rpa_your_key
   cd books/sygl-book/sygl-manga
   python3 tools/gen.py health                       # confirm workers are ready
   python3 tools/gen.py txt2img --prompt "Bal on a roof, ..." --out test.png --seed 42
   python3 tools/gen.py inpaint --base test.png --out fixed.png \
       --ellipse 808 596 930 690 \
       --prompt "left forearm ends in a rounded stump, no hand, no fingers"
   ```
   `txt2img` auto-appends the locked STYLE block; add `--raw` to use your prompt verbatim.
   Cost ≈ 2¢/image; $0 idle. **Rotate/delete the API key when done** — it can spend money.
4. **Follow the canon** in `chapter-01-storyboard.md` (Bal = stump + no sygl; spot-color
   sygls; mausoleum BEHIND orphanage; kids in FRONT; Bal ALONE) and the locked designs in
   `CHARACTER-LOCK.md`. Verify each panel against the SETTING/PROP CONTINUITY checklist.

## VISUAL STYLE (locked 2026-07-14)
**Monochrome manga + SPOT-COLOR sygls/magyk.** Pages are black-and-white ink + screentone;
the ONLY color is the sygls and actively-cast magyk, each in its element's colour. This makes
the magic system instantly readable and lets Bal's Blood powers pop later.

**Element → colour map** (house sygl on the palm + that element's aerial glyphs when casting):
| Element / sygl | Colour |
|---|---|
| **Blood** (Amelia; Bal after regrowth) | crimson red |
| **Terra** (Posy) | green |
| **Tempus** (storm; Viridia) | electric blue |
| **Waves** (Lora) | deep teal/blue |
| **Duality** (Aren/Nera) | TBD (split/gold?) |
| others | TBD as they appear |

Notes: In **Ch.1** the only colour moments are Posy's green Terra mark (flashback) and any
marked hand in the crowd — Bal is UNMARKED and his stump-forced levitation is NOT an element,
so it carries **no sygl colour** (draw it as plain B/W strain/glow at the stump). Colour enters
the book properly with the Blood sygl later.

## Pipeline at a glance
Prose chapter (finalized in `../manuscript/`) → panel script → generate panels
on RunPod (ComfyUI + FLUX) → letter speech bubbles → assemble page. Character
consistency is the next milestone (lock Bal's seed/prompt, then IP-Adapter/LoRA).

---

## ✅ WORKING CONFIG (confirmed 2026-07-14)
- **Serverless** endpoint from the Hub → **"ComfyUI" release 5.8.5** (NOT 5.8.6).
  The 5.8.6 FLUX.1-dev build crash-looped (workers unhealthy, empty container
  logs, jobs stuck IN_QUEUE) even with a valid HF token + granted gated access.
  The **5.8.5** release boots clean (model baked in, no gated download) and
  generated Bal in ~20s.
- GPU: 24 GB · Active workers 0 · Max 1 · FlashBoot on · no env vars needed.
- Driven purely by API (`/run` + poll `/status/{id}`), images returned as
  base64 in `output.images[].data`. Working FLUX t2i workflow (CheckpointLoader
  `flux1-dev-fp8.safetensors` → CLIPTextEncode ×2 → EmptySD3LatentImage →
  KSampler(cfg 1.0, euler, simple, 20 steps) → VAEDecode → SaveImage).
- Cost: ~2¢ per image; $0 while idle (serverless). No pod to shut down.
- Prompt tip: add `signature, border, text` to the NEGATIVE to kill the garbled
  autograph/frame FLUX sometimes adds.
- API key is NOT stored here (secret). Endpoint ID + key are passed per session.

---


Goal: rent an RTX 4090 by the hour (~$0.34/hr), run ComfyUI, and generate
**consistent** manga panels of Bal & co. Pay only while the pod runs; shut it
down and you pay nothing.

Character reference art already in repo: `books/sygl-book/sygl-manga/bal-manga.png`.
Generated panels save into `books/sygl-book/sygl-manga/`.

---

## PHASE 0 — Account & credit (one time, ~5 min)
1. Go to **runpod.io** → Sign up (Google/GitHub login is fine).
2. **Billing → Add Credit.** Load **$10** (card or crypto). No subscription;
   it's a prepaid balance that drains only while a pod runs.
3. (Optional) Billing → set a low-balance email alert so you never overspend.

## PHASE 1 — Deploy the pod (~3 min)
1. Left menu → **Pods → Deploy** (a.k.a. "+ GPU Pod" / "Deploy a Pod").
2. **GPU:** pick **RTX 4090** (Community Cloud = cheapest, ~$0.34/hr).
3. **Template:** in the template search, choose a **ComfyUI** template.
   Good ones: "ComfyUI" by RunPod, or "AI-Dock ComfyUI", or "Better ComfyUI
   (with Manager)". Any that says ComfyUI + exposes an HTTP port works.
4. **Disk:** bump **Container Disk to ~20 GB** and **Volume Disk to ~30 GB**
   (models are big; a volume persists your files between sessions).
5. Click **Deploy On-Demand.** Wait for status → **Running** (1–3 min).

## PHASE 2 — Open ComfyUI (~1 min)
1. On the pod card click **Connect.**
2. Click the **HTTP port** button (usually **:8188** or "Connect to HTTP
   Service [Port 8188]"). ComfyUI opens in a new browser tab.
   - If you see a node graph, you're in.

## PHASE 3 — Load a manga/anime model (~3 min, one time)
ComfyUI needs a checkpoint. Use the **Manager** (most templates include it):
1. Click **Manager** (button in the ComfyUI menu) → **Model Manager** /
   **Install Models.**
2. Search and install an anime/manga checkpoint. Recommended, in order:
   - **"Illustrious"** or **"NoobAI XL"** (modern anime, great lineart), OR
   - **"Anything V5"** / **"AOM3"** (classic anime), OR
   - **manga/lineart-specialized** checkpoint if listed.
3. After download, **Refresh** so the model appears in the "Load Checkpoint"
   node dropdown.

If the template has NO Manager: use the terminal (Pod → Connect → Web Terminal)
and download a checkpoint into `/workspace/ComfyUI/models/checkpoints/`. Ask me
and I'll give you an exact `wget` command for a specific model.

## PHASE 4 — First panel (text-to-image)
1. In ComfyUI, load the **default text-to-image workflow** (Manager → "Load
   Default", or it's already on screen).
2. Set **Load Checkpoint** → your anime model.
3. **Positive prompt** (example for a Bal portrait):
   ```
   manga, monochrome, greyscale, screentone, clean lineart, 1boy, 16 years old,
   messy dark hair, kind determined eyes, worn traveler tunic, left hand raised
   with glowing sigil on palm, upper body, dramatic lighting, high detail
   ```
4. **Negative prompt:**
   ```
   color, lowres, bad anatomy, bad hands, extra fingers, watermark, signature,
   text, blurry, deformed
   ```
5. **Resolution:** 832x1216 (portrait panel) or 1216x832 (wide panel).
6. Click **Queue Prompt.** First run loads the model (slow, ~30s); after that
   each image is a few seconds. Right-click the image → Save.

## PHASE 5 — CHARACTER CONSISTENCY (the whole point)
Two ways, easiest first:

**A) Reference image (fast, no training):**
- Install **IP-Adapter** via Manager (custom node "ComfyUI_IPAdapter_plus").
- Load an IP-Adapter workflow, feed it `bal-manga.png` as the reference, and it
  biases every new image toward Bal's face/design. Good for "same-ish" Bal.

**B) Train a Bal LoRA (best, ~30 min once):**
- Once we have 10–20 approved Bal images (front/side/expressions), train a small
  character LoRA (kohya_ss template on RunPod). After that, adding `bal` to any
  prompt reproduces him exactly, any pose, forever.
- We build the training set FROM phase 4/5A outputs. Chicken-and-egg solved:
  generate a bunch, pick the best, lock the face with a LoRA.

**C) Exact posing (optional):** ControlNet (OpenPose/lineart) lets you dictate
the exact pose/panel composition. Install via Manager when we get to staging
real pages.

## PHASE 6 — SHUT DOWN (don't skip — this is how you save money)
- When done: pod card → **Stop** (keeps your volume/files, stops billing for
  GPU) or **Terminate** (deletes everything, cheapest).
- **Stopped** pods still cost a tiny amount for stored volume; **Terminated**
  costs nothing. If you saved your images/models to the volume and want them
  next time, use **Stop**. Otherwise download your art and **Terminate**.

---

## Cost reality check
- RTX 4090 ≈ **$0.34/hr**. A 2–3 hr session ≈ **$0.70–$1.00**.
- $10 ≈ ~30 GPU-hours = many chapters of panels.
- You are NEVER billed while the pod is Stopped/Terminated.

## Where Claude helps
- Exact prompts per panel (from the Chapter 1 panel script).
- `wget` commands for specific models if Manager is missing.
- Tuning negatives/settings when hands or faces come out wrong.
- Building the LoRA training set and settings.
- Programmatic page layout + speech-bubble lettering after panels are made.
