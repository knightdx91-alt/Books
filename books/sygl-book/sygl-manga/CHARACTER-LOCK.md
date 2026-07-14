# Sygl Manga — LOCKED CHARACTER REFERENCES (Chapter 1)

Canonical design per character. Generate every panel to MATCH these. (True cross-panel
face-lock would need an IP-Adapter/LoRA — see note; for now, prompt-match + img2img from
these refs, and re-roll faces that drift too far.)

| Character | LOCKED reference | Canon notes |
|---|---|---|
| **Bal (Pre-Regrowth)** | `REF-bal-preregrowth.png` | 16, messy DARK hair, kind even face, worn hand-me-downs, small backpack. LEFT hand = STUMP. NO sygl anywhere. (Ch.1–2 only; regrown-hand Bal is a separate future ref.) |
| **Fredrick** | `REF-fredrick.png` | 16, NEAT PALE/LIGHT hair + freckles (deliberately UNLIKE Bal), buttoned shirt, easy grin, carries spellbooks + a trunk. Has a sygl (palm). One flashback panel (p.5). |
| **Posy** | `REF-posy.png` | ~10, short dark bob, plain worn dress, shy/startled. Gets the GREEN Terra sygl on her PALM (spot-color green). One flashback panel (p.3). |
| **The Statue (Amelia's likeness)** | `REF-statue-amelia-likeness.png` | Tall pale robed stone figure, FACE TURNED AWAY (never show her face in Ch.1 — protects the Ch.2 reveal). Also serves as the temple-interior establishing ref. |
| **Amelia** | — (DEFERRED) | Unseen in Ch.1 (voice only). Full design built with Ch.2. The statue foreshadows her silhouette. |
| **Orphan kids (bg)** | `design-orphans-yard.png` (style) | Generic worn-clothes orphans, TINY/distant, never beside Bal. One may show a palm-sygl. |

## Consistency mechanism (honest note)
Plain FLUX prompting drifts faces panel-to-panel. To hold these locked designs we will:
1. Prompt-match tightly to the ref descriptions above, and
2. Use FLUX img2img (low denoise) FROM the locked ref for close-up/face panels when needed.
3. If drift becomes a real problem across the full chapter, train a per-character LoRA
   (Option B) for a permanent lock. Deferred until we see how far prompt+img2img gets us.

## Status: Bal ✅ · Fredrick ✅ · Posy ✅ · Statue ✅ · Amelia ⏭ (Ch.2)
