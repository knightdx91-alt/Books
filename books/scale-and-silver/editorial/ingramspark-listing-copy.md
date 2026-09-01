# IngramSpark listing copy — *A Bond of Scale and Silver*

Everything that goes in the IngramSpark setup form's text fields. Ingram has **two
separate description fields** and they are not interchangeable:

- **Description** — the long one (~4,000 char limit). This is what appears on Amazon,
  Barnes & Noble and the rest. Section below.
- **Short Description** — a brief summary for Ingram's own catalogs and some online
  sites (~350 chars). Different section, further down. Ingram asks for key selling
  points here, and explicitly no author bio, no excerpt, no URLs.

---

## DESCRIPTION field (the long one)

The same copy works at KDP/Apple/Kobo.

Written to Ingram's guidance for that field: consumer-friendly, and with the
Keyword-field terms worked into the prose so the description and the keywords
reinforce each other for discovery. Ingram also suggests bolding key sentences —
**the author chose plain text**, so the bolded variant is kept collapsed at the
bottom rather than used.

Built from the approved back-cover copy, so the listing and the printed cover agree.

---

## Paste this — plain text, one paragraph per line, real em dashes

```text
She was born to be a secret. The world is about to make her a war.

Amelia has never been allowed outside.

The first vampire born — not made — in a thousand years, she is her mother the Queen's cherished, forbidden secret: a girl with blood magyk that should not exist, kept behind a bolt because her very existence could shatter the treaty holding three peoples apart. She wants one thing the world will never grant her — to be seen.

Then a grief-poisoned schemer unveils her before both courts, and the war begins.

On the run at last, Amelia crosses paths with Korvan, the shifter chief's outcast son. His first change makes him the one creature more hunted than she is: a dragon out of dead legend, a clan of one. Thrown together on a brutal road with the war closing behind them, hunted by silver and by worse things than silver, two exiles learn each other in a slow burn that takes the whole journey to catch.

But the bond they choose is not fated. No one hands it to them. And being finally seen will cost Amelia everything she loves.

A dark adult romantasy of dangerous devotion, chosen love, and the terrible price of the truth.

For readers of Carissa Broadbent and Danielle L. Jensen, with the plain-spoken menace of Anne Bishop's Black Jewels. A complete standalone fantasy romance — no cliffhanger, no sequel required.

What to expect: dual POV, slow-burn forced proximity, a chosen bond rather than fated mates, vampire courts and dragon shifters, morally grey politics, a dangerous heroine who is never a victim, and an earned, bittersweet ending rather than a tidy happily-ever-after.

Content advisory: Adult (18+). Explicit sexual content (two open-door scenes), battlefield violence, on-page grief and loss. No sexual violence.
```

Deliberately not hard-wrapped: these paste into a web form as clean paragraphs.

**Size:** 1751 characters, 1759 bytes. The Description field's
~4,000 limit leaves ample room either way, but note the gap between the two numbers —
the em dashes cost 3 bytes each. The Short Description field below is capped in
**bytes**, not characters, which is why that one is written in pure ASCII.

If a form mangles the em dashes, replace them with a spaced hyphen rather than letting
a mojibake character reach the live listing.

---

## SHORT DESCRIPTION field

**Hard limit: 250 BYTES** (confirmed in the form — not characters). That distinction
matters: in UTF-8 an em dash costs 3 bytes and a curly quote 3, so a 250-character
string with typographic punctuation can be 270+ bytes and get truncated or rejected.
Everything below is **pure ASCII**, so bytes equal characters and what you see is what
fits. Keep it that way if you edit it.

Ingram asks for key selling points here and forbids author bio, excerpt and URLs.

**Note on "key selling points":** this book has no awards, no illustrations and no
bonus material to cite, so the points carrying it are the premise hook (first
natural-born vampire plus a dragon clan-of-one), the **standalone** status, and the
**chosen-not-fated** differentiator that separates it from default romantasy. Do not
invent an award to fill the space — Ingram's catalog is trade-facing and a fabricated
credit is worse than none.

### Use this — 242 bytes

```text
The first vampire born, not made, in a thousand years, Amelia is the secret that starts a war. On the run she meets an outcast whose first shift makes him a dragon out of dead legend. A standalone adult romantasy: chosen love, not fated. 18+.
```

### Alternative, 244 bytes — leads on her rather than the premise

```text
Amelia is the first vampire born, not made, in a thousand years: a hidden daughter whose existence can start a war. Exposed and hunted, she meets an outcast who shifts into a dragon out of dead legend. Standalone adult romantasy. Dual POV. 18+.
```

At this length the comp author does not fit alongside the premise, and the premise is
the stronger hook — it goes in the long Description instead.

---

## KEYWORD field

Semicolon-separated, 10 terms, 240 characters / 240 bytes, pure ASCII:

```text
adult romantasy; vampire romance; dragon shifter romance; slow burn fantasy romance; standalone fantasy romance; dark fantasy romance; forced proximity romance; spicy fantasy romance; hidden royal fantasy romance; morally grey love interest
```

Every one is supported by the book and appears in, or is a direct component of, the
Description copy — which is what Ingram means by having the two reinforce each other.

### Two terms deliberately NOT used

- **`fated mates`** — high-volume in romantasy, and actively wrong here. The book's
  stated differentiator is a bond that is *chosen, not fated*; the positioning notes
  call that out as what separates it from default romantasy. Using the term would pull
  in exactly the readers set up to be disappointed, and disappointed readers leave
  one-star reviews. Volume is not worth a mismatch.
- **`enemies to lovers`** — also high-volume, also inaccurate. Amelia and Korvan are
  two hunted people thrown together, not adversaries. `forced proximity romance` is
  the honest version of that search and is in the list.

Comp authors — **Anne Bishop, Carissa Broadbent, Danielle L. Jensen** — must not go in
this field either. Another author's name as a backend keyword breaches Amazon's terms
and can get a listing suppressed. They belong in the Description as positioning, where
they already are.

## BISAC categories

- `FIC009120` FICTION / Fantasy / Romance — primary
- `FIC027120` FICTION / Romance / Fantasy
- `FIC009050` FICTION / Fantasy / Dark Fantasy

## Two calls worth keeping

- **"Standalone" is stated plainly.** Romantasy readers have been burned by
  book-one-of-six; saying so converts browsers rather than limiting the book.
- **The bittersweet-ending line stays.** Romance readers treat a happily-ever-after as
  a genre promise, and this book deliberately withholds a tidy one. Flagging it loses
  a few sales and prevents the one-star "I was misled" reviews. Concealing it costs
  more than it earns. To sell harder and accept that risk, cut the final clause of the
  *What to expect* line.

<details>
<summary>HTML variant with bolded key sentences — unused, kept for reference</summary>

Ingram accepts basic HTML in this field and passes it through to Amazon. If bolding is
ever wanted, most of the effect comes from the first line and the "standalone" line
alone.

```html
<p><b>She was born to be a secret. The world is about to make her a war.</b></p>

<p>Amelia has never been allowed outside.</p>

<p><b>The first vampire born&mdash;not made&mdash;in a thousand years, she is her mother the Queen's cherished, forbidden secret:</b> a girl with blood magyk that should not exist, kept behind a bolt because her very existence could shatter the treaty holding three peoples apart. She wants one thing the world will never grant her&mdash;to be seen.</p>

<p>Then a grief-poisoned schemer unveils her before both courts, and the war begins.</p>

<p>On the run at last, Amelia crosses paths with Korvan, the shifter chief's outcast son. <b>His first change makes him the one creature more hunted than she is: a dragon out of dead legend, a clan of one.</b> Thrown together on a brutal road with the war closing behind them, hunted by silver and by worse things than silver, two exiles learn each other in a slow burn that takes the whole journey to catch.</p>

<p><b>But the bond they choose is not fated. No one hands it to them.</b> And being finally seen will cost Amelia everything she loves.</p>

<p><i>A dark adult romantasy of dangerous devotion, chosen love, and the terrible price of the truth.</i></p>

<p><b>For readers of Carissa Broadbent and Danielle L. Jensen</b>, with the plain-spoken menace of Anne Bishop's <i>Black Jewels</i>. <b>A complete standalone fantasy romance&mdash;no cliffhanger, no sequel required.</b></p>

<p><b>What to expect:</b> dual POV &middot; slow-burn forced proximity &middot; a chosen bond rather than fated mates &middot; vampire courts and dragon shifters &middot; morally grey politics &middot; a dangerous heroine who is never a victim &middot; an earned, bittersweet ending rather than a tidy happily-ever-after.</p>

<p><b>Content advisory:</b> Adult (18+). Explicit sexual content (two open-door scenes), battlefield violence, on-page grief and loss. No sexual violence.</p>
```
</details>
