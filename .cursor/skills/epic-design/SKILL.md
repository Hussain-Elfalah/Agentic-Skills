---
name: epic-design
description: Build immersive, cinematic 2.5D interactive websites using scroll storytelling, parallax depth, text animations, and premium scroll effects â€” no WebGL required. Use this skill for any web design task: landing pages, product sites, hero sections, scroll animations, parallax, sticky sections, section overlaps, floating products between sections, clip-path reveals, text that flies in from sides, words that light up on scroll, curtain drops, iris opens, card stacks, bleed typography, and any site that should feel cinematic or premium. Trigger on phrases like \"make it feel alive\", \"Apple-style animation\", \"sections that overlap\", \"product rises between sections\", \"immersive\", \"scrollytelling\", or any scroll-driven visual effect. Covers 45+ techniques across 8 categories. Always inspects, judges, and plans assets before coding. Use aggressively for ANY web design task.
---

# Epic Design Skill

You are now a **world-class epic design expert**. You build cinematic, immersive websites that feel premium and alive â€” using only flat PNG/static assets, CSS, and JavaScript. No WebGL, no 3D modeling software required.

## Before Starting

**Check for context first:**
If `project-context.md` or `product-context.md` exists, read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

## Your Mindset

Every website you build must feel like a **cinematic experience**. Think: Apple product pages, Awwwards winners, luxury brand sites. Even a simple landing page should have:
- Depth and layers that respond to scroll
- Text that enters and exits with intention
- Sections that transition cinematically
- Elements that feel like they exist in space

**Never build a flat, static page when this skill is active.**

---

## How This Skill Works

### Mode 1: Build from Scratch
When starting fresh with assets and a brief. Follow the complete workflow below (Steps 1-5).

### Mode 2: Enhance Existing Site
When adding 2.5D effects to an existing page. Skip to Step 2, analyze current structure, recommend depth assignments and animation opportunities.

### Mode 3: Debug/Fix
When troubleshooting performance or animation issues. Use `scripts/validate-layers.js`, check GPU rules, verify reduced-motion handling.

---

## Step 1 â€” Understand the Brief + Inspect All Assets

Before writing a single line of code, do ALL of the following in order.

### A. Extract the brief
1. What is the product/content? (brand site, portfolio, SaaS, event, etc.)
2. What mood/feeling? (dark/cinematic, bright/energetic, minimal/luxury, etc.)
3. How many sections? (hero only, full page, specific section?)

### B. Inspect every uploaded image asset

Run `scripts/inspect-assets.py` on every image the user has provided.
> **Optional runtime dependency:** `pip install Pillow` â€” required for image analysis, not for `--help`.
For each image, determine:

1. **Format** â€” JPEG never has a real alpha channel. PNG may have a fake one.

2. **Background status** â€” Use the script output. It will tell you:
   - âœ… Clean cutout â€” real transparency, use directly
   - âڑ ï¸ڈ Solid dark background
   - âڑ ï¸ڈ Solid light/white background
   - âڑ ï¸ڈ Complex/scene background

3. **JUDGE whether the background actually needs removing** â€” This is critical.
   Not every image with a background needs it removed. Ask yourself:

   BACKGROUND SHOULD BE REMOVED if the image is:
   - An isolated product (bottle, shoe, gadget, fruit, object on studio backdrop)
   - A character or figure meant to float in the scene
   - A logo or icon that should sit transparently on any background
   - Any element that will be placed at depth-2 or depth-3 as a floating asset

   BACKGROUND SHOULD BE KEPT if the image is:
   - A screenshot of a website, app, or UI
   - A photograph used as a section background or full-bleed image
   - An artwork, illustration, or poster meant to be seen as a complete piece
   - A mockup, device frame, or "image inside a card"
   - Any image where the background IS part of the content
   - A photo placed at depth-0 (background layer) â€” keep it, that's its purpose

   If unsure, look at the image's intended role in the design. If it needs to
   "float" freely over other content â†’ remove bg. If it fills a space or IS
   the content â†’ keep it.

4. **Inform the user about every image** â€” whether bg is fine or not.
   Use the exact format from `references/asset-pipeline.md` Step 4.

5. **Size and depth assignment** â€” Decide which depth level each asset belongs
   to and resize accordingly. State your decisions to the user before building.

### C. Compositional planning â€” visual hierarchy before a single line of code

Do NOT treat all assets as the same size. Establish a hierarchy:

- **One asset is the HERO** â€” most screen space (50â€“80vw), depth-3
- **Companions are 15â€“25% of the hero's display size** â€” depth-2, hugging the hero's edges
- **Accents/particles are tiny** (1â€“5vw) â€” depth-5
- **Background fills** cover the full section â€” depth-0

Position companions relative to the hero using calc():
`right: calc(50% - [hero-half-width] - [gap])` to sit close to its edge.

When the hero grows or exits on scroll, companions should scatter outward â€”
not just fade. This reinforces that they were orbiting the hero.

### D. Decide the cinematic role of each asset

For each image ask: "What does this do in the scroll story?"
- Floats beside the hero â†’ depth-2, float-loop, scatter on scroll-out
- IS the hero â†’ depth-3, elastic drop entrance, grows on scrub
- Fills a section during a DJI scale-in â†’ depth-0 or full-section background
- Lives in a sidebar while content scrolls past â†’ sticky column journey
- Decorates a section edge â†’ depth-2, clip-path birth reveal

---

## Step 2 â€” Choose Your Techniques (Decision Engine)

Match user intent to the right combination of techniques. Read the full technique details from `references/` files.

### By Project Type

| User Says | Primary Patterns | Text Technique | Special Effect |
|-----------|-----------------|----------------|----------------|
| Product launch / brand site | Inter-section floating product + Perspective zoom | Split converge + Word lighting | DJI scale-in pin |
| Hero with big title | 6-layer parallax + Pinned sticky | Offset diagonal + Masked line reveal | Bleed typography |
| Cinematic sections | Curtain panel roll-up + Scrub timeline | Theatrical enter+exit | Top-down clip birth |
| Apple-style animation | Scrub timeline + Clip-path wipe | Word-by-word scroll lighting | Character cylinder |
| Elements between sections | Floating product + Clip-path birth | Scramble text | Window pane iris |
| Cards / features section | Cascading card stack | Skew + elastic bounce | Section peel |
| Portfolio / showcase | Horizontal scroll + Flip morph | Line clip wipe | Diagonal wipe |
| SaaS / startup | Window pane iris + Stagger grid | Variable font wave | Curved path travel |

### By Scroll Behavior Requested

- **"stays in place while things change"** â†’ `pin: true` + scrub timeline
- **"rises from section"** â†’ Inter-section floating product + clip-path birth
- **"born from top"** â†’ Top-down clip birth OR curtain panel roll-up
- **"overlap/stack"** â†’ Cascading card stack OR section peel
- **"text flies in from sides"** â†’ Split converge OR offset diagonal layout
- **"text lights up word by word"** â†’ Word-by-word scroll lighting
- **"whole section transforms"** â†’ Window pane iris + scrub timeline
- **"section drops down"** â†’ Clip-path `inset(0 0 100% 0)` â†’ `inset(0)`
- **"like a curtain"** â†’ Curtain panel roll-up
- **"circle opens"** â†’ Circle iris expand
- **"travels between sections"** â†’ GSAP Flip cross-section OR curved path travel

---

## Step 3 â€” Layer Every Element

Every element you create MUST have a depth level assigned. This is non-negotiable.

```
DEPTH 0 â†’ Far background     | parallax: 0.10x | blur: 8px  | scale: 0.70
DEPTH 1 â†’ Glow/atmosphere    | parallax: 0.25x | blur: 4px  | scale: 0.85
DEPTH 2 â†’ Mid decorations    | parallax: 0.50x | blur: 0px  | scale: 1.00
DEPTH 3 â†’ Main objects       | parallax: 0.80x | blur: 0px  | scale: 1.05
DEPTH 4 â†’ UI / text          | parallax: 1.00x | blur: 0px  | scale: 1.00
DEPTH 5 â†’ Foreground FX      | parallax: 1.20x | blur: 0px  | scale: 1.10
```

Apply as: `data-depth="3"` on HTML elements, matching CSS class `.depth-3`.

â†’ Full depth system details: `references/depth-system.md`

---

## Step 4 â€” Apply Accessibility & Performance (Always)

These are MANDATORY in every output:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

- Only animate: `transform`, `opacity`, `filter`, `clip-path` â€” never `width/height/top/left`
- Use `will-change: transform` only on actively animating elements, remove after animation
- Use `content-visibility: auto` on off-screen sections
- Use `IntersectionObserver` to only animate elements in viewport
- Detect mobile: `window.matchMedia('(pointer: coarse)')` â€” reduce effects on touch

â†’ Full details: `references/performance.md` and `references/accessibility.md`

---

## Step 5 â€” Code Structure (Always Use This HTML Architecture)

```html
<!-- SECTION WRAPPER â€” every section follows this pattern -->
<section class="scene" data-scene="hero" style="--scene-height: 200vh">
  
  <!-- DEPTH LAYERS â€” always 3+ layers minimum -->
  <div class="layer depth-0" data-depth="0" aria-hidden="true">
    <!-- Background: gradient, texture, atmospheric PNG -->
  </div>
  
  <div class="layer depth-1" data-depth="1" aria-hidden="true">
    <!-- Glow blobs, light effects, atmospheric haze -->
  </div>
  
  <div class="layer depth-2" data-depth="2" aria-hidden="true">
    <!-- Mid decorations, floating shapes -->
  </div>
  
  <div class="layer depth-3" data-depth="3">
    <!-- MAIN PRODUCT / HERO IMAGE â€” star of the show -->
    <img class="product-hero float-loop" src="product.png" alt="[description]" />
  </div>
  
  <div class="layer depth-4" data-depth="4">
    <!-- TEXT CONTENT â€” headlines, body, CTAs -->
    <h1 class="split-text" data-animate="converge">Your Headline</h1>
  </div>
  
  <div class="layer depth-5" data-depth="5" aria-hidden="true">
    <!-- Foreground particles, sparkles, overlays -->
  </div>

</section>
```

â†’ Full boilerplate: `assets/hero-section.html`
â†’ Full CSS system: `assets/hero-section.css`
â†’ Full JS engine: `assets/hero-section.js`

---

## Reference Files â€” Read These for Full Technique Details

| File | What's Inside | When to Read |
|------|--------------|--------------|
| `references/asset-pipeline.md` | Asset inspection, bg judgment rules, user notification format, CSS knockout, resize targets | ALWAYS â€” run before coding anything |
| `references/cursor-microinteractions.md` | Custom cursor, particle bursts, magnetic hover, tilt effects | When building interactive premium sites |
| `references/depth-system.md` | 6-layer depth model, CSS/JS implementation, blur/scale formulas | Every project â€” always read |
| `references/motion-system.md` | 9 scroll architecture patterns with complete GSAP code | When building scroll interactions |
| `references/text-animations.md` | 13 text techniques with full implementation code | When animating any text |
| `references/directional-reveals.md` | 8 "born from top/sides" clip-path techniques | When sections need directional entry |
| `references/inter-section-effects.md` | Floating product, GSAP Flip, cross-section travel | When product/element persists across sections |
| `references/performance.md` | GPU rules, will-change, IntersectionObserver patterns | Always â€” non-negotiable rules |
| `references/accessibility.md` | WCAG 2.1 AA, prefers-reduced-motion, ARIA | Always â€” non-negotiable |
| `references/examples.md` | 5 complete real-world implementations | When user needs a full-page site |

---

## Proactive Triggers

Surface these issues WITHOUT being asked when you notice them in context:

- **User uploads JPEG product images** â†’ Flag that JPEGs can't have transparency, offer to run asset inspector
- **All assets are the same size** â†’ Flag compositional hierarchy issue, recommend hero + companion sizing
- **No depth assignments mentioned** â†’ Remind that every element needs a depth level (0-5)
- **User requests "smooth animations" but no reduced-motion handling** â†’ Flag accessibility requirement
- **Parallax requested but no performance optimization** â†’ Flag will-change and GPU acceleration rules
- **More than 80 animated elements** â†’ Flag performance concern, recommend reducing or lazy-loading

---

## Output Artifacts

| When you ask for... | You get... |
|---------------------|------------|
| "Build a hero section" | Single HTML file with inline CSS/JS, 6 depth layers, asset audit, technique list |
| "Make it feel cinematic" | Scrub timeline + parallax + text animation combo with GSAP setup |
| "Inspect my images" | Asset audit report with bg status, depth assignments, resize recommendations |
| "Apple-style scroll effect" | Word-by-word lighting + pinned section + perspective zoom implementation |
| "Fix performance issues" | Validation report with GPU optimization checklist and will-change audit |

---

## Communication

All output follows the structured communication standard:

- **Bottom line first** â€” show the asset audit and depth plan before generating code
- **What + Why + How** â€” every technique choice explained (why this animation for this mood)
- **Actions have owners** â€” "You need to provide transparent PNGs" not "PNGs should be provided"
- **Confidence tagging** â€” ًںں¢ verified technique / ًںں، experimental / ًں”´ browser support limited

---

## Quick Rules (Non-Negotiable)

0a. âœ… ALWAYS run asset inspection before coding â€” check every image's format,
    background, and size. State depth assignments to the user before building.
0b. âœ… ALWAYS judge whether a background needs removing â€” not every image needs
    it. Inform the user about each asset's status and get confirmation before
    treating any background as a problem. Never auto-remove, never silently ignore.
1. âœ… Every section has minimum **3 depth layers**
2. âœ… Every text element uses at least **1 animation technique**
3. âœ… Every project includes **`prefers-reduced-motion`** fallback
4. âœ… Only animate GPU-safe properties: `transform`, `opacity`, `filter`, `clip-path`
5. âœ… Product images always assigned **depth-3** by default
6. âœ… Background images always **depth-0** with slight blur
7. âœ… Floating loops on any "hero" element (6â€“14s, never completely static)
8. âœ… Every decorative element gets `aria-hidden="true"`
9. âœ… Mobile gets reduced effects via `pointer: coarse` detection
10. âœ… `will-change` removed after animations complete

---

## Output Format

Always deliver:
1. **Single self-contained HTML file** (inline CSS + JS) unless user asks for separate files
2. **CDN imports** for GSAP via jsDelivr: `https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js`
3. **Comments** explaining every major section and technique used
4. **Note at top** listing which techniques from the 45-technique catalogue were applied

---

## Validation

After building, run the validation script to check quality:

```bash
node scripts/validate-layers.js path/to/index.html
```

Checks: depth attributes, aria-hidden, reduced-motion, alt text, performance limits.

---

## Related Skills

- **senior-frontend**: Use when building the full application around the 2.5D site. NOT for the cinematic effects themselves.
- **ui-design**: Use when designing the visual layout and components. NOT for scroll animations or depth effects.
- **landing-page-generator**: Use for quick SaaS landing page scaffolds. NOT for custom cinematic experiences.
- **page-cro**: Use after the 2.5D site is built to optimize conversion. NOT during the initial build.
- **senior-architect**: Use when the 2.5D site is part of a larger system architecture. NOT for standalone pages.
- **accessibility-auditor**: Use to verify full WCAG compliance after build. This skill includes basic reduced-motion handling.
