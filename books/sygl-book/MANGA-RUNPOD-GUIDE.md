# Sygl Manga — RunPod + ComfyUI Setup Guide

Goal: rent an RTX 4090 by the hour (~$0.34/hr), run ComfyUI, and generate
**consistent** manga panels of Bal & co. Pay only while the pod runs; shut it
down and you pay nothing.

Character reference art already in repo: `books/sygl-book/bal-manga.png`.

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
