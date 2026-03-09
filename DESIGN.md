# Dennis Bakhuis — Personal Website Design

## Overview
A single-page personal website with a cinematic intro animation, built as a single `index.html` file with inline CSS/JS. No build tools or frameworks — pure HTML, CSS, and vanilla JavaScript.

## Intro Sequence

1. **Initial state**: Full white screen with "Dennis Bakhuis" centered in large, bold black font.
2. **Three stripes enter**: Three horizontal black stripes slide in from different directions (e.g. left, right, bottom) and expand to fill the screen.
3. **Photo reveal**: The three stripes together form **one single image** — a black-and-white photograph of Dennis, split across the three bands. Each stripe shows its corresponding third of the photo, so when all three have entered, the full picture is visible.
4. **Color inversion**: Once the stripes have fully covered the screen, the color scheme reverses — the page transitions to a black background with white text.

## Stripe Details
- Three horizontal bands dividing the viewport into roughly equal thirds.
- Each stripe slides in with a slight stagger delay (e.g. 200ms apart).
- All three stripes share the **same background image**, each using `background-position` to show its respective third (top, middle, bottom) so they combine into one seamless photo.
- The photo is displayed with `filter: grayscale(100%)` to ensure black-and-white appearance.
- On each page load, a photo is randomly selected from a pool in the `images/` directory. Initially, the pool will contain just **one photo**.
- The photo may have a subtle zoom or parallax while the stripes are animating.

## Page Structure

### Header / Nav
- Minimal sticky navigation that appears after the intro completes.
- Contains: name/logo (left), nav links (right).

### Sections (scrollable, white-on-black)
1. **Hero** — Name, tagline, brief one-liner about Dennis.
2. **About** — Short bio, key skills, current role.
3. **Work / Projects** — Selected portfolio items with thumbnails and descriptions.
4. **Writing / Blog** — Links to recent articles or posts.
5. **Contact** — Email, social links, availability status.

### Footer
- Minimal footer with copyright and social icons.

## Technical Plan

### File Structure
```
/
├── index.html          # Single-page site (HTML + inline CSS + JS)
├── images/             # Black-and-white photos for the intro stripes
│   ├── photo1.jpg
│   ├── photo2.jpg
│   ├── ...
├── DESIGN.md           # This file
└── README.md           # (optional) project readme
```

### Animation Implementation
- Use CSS `@keyframes` for stripe slide-in and expansion.
- JavaScript handles: random photo selection, animation sequencing, removing the intro overlay after completion.
- `IntersectionObserver` for scroll-triggered section animations post-intro.

### Responsiveness
- Mobile-first approach with breakpoints at 768px and 1200px.
- On smaller screens, stripes may enter vertically instead of horizontally.
- Font sizes and spacing scale with `clamp()`.

### Performance
- Lazy-load images below the fold.
- Preload the intro stripe photos so the animation starts without delay.
- Keep total page weight under 2MB (optimized/compressed images).

## Style Reference: sharm.framer.website

The overall look and feel should draw from this Framer template:

### Color Palette
- **Primary dark**: `#1a1a1a` (near-black) — used as the main background after the intro inversion.
- **Primary light**: `#fff` (white) — text color post-intro, background during intro.
- **Accent/warm neutral**: `#e5e3de` (warm beige) — for contrast sections or subtle backgrounds.
- **Link/accent color**: `#09f` (bright cyan) — interactive elements, hover states.

### Typography
- **Primary font**: DM Sans (400–700) for body text.
- **Secondary/display font**: Inter / Inter Display for headings and large text.
- Clean hierarchy: large bold display headings, medium weight body, light captions.
- Use `font-display: swap` for performance.

### Layout & Spacing
- Generous whitespace: 150–300px vertical padding between major sections.
- 8px base grid (common gaps: 24px, 32px, 56px).
- Content width ~90% of viewport, max-width container for readability.
- Flex-based centering and alignment throughout.

### Navigation
- Fixed/sticky top nav bar with name/logo left, links right.
- Small fixed CTA button in the bottom-right corner.

### Visual Details
- Circular profile images (border-radius: 50%).
- Subtle 1px dividers between sections (opacity ~16%).
- `will-change: transform` on animated elements for smooth motion.
- Staggered z-index layering for depth.
- Overflow hidden on image containers.

### Responsive Breakpoints
- `≥1600px` — full desktop
- `1200–1599px` — standard desktop
- `810–1199px` — tablet
- `≤810px` — mobile

### Hover & Interaction
- Links: underlined cyan with hover state changes.
- Smooth transform-based animations and transitions.

## Open Questions
- ~~Exact photo pool size~~ — Starting with 1 photo; more can be added later.
- Should the intro replay on revisit or only show once per session?
- Should sections have scroll-snap behavior?
