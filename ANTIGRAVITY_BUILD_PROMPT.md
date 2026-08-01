# Prompt: paste this into Antigravity

---

I have a complete static website (plain HTML/CSS/JS, no build tooling, no framework) for a project-management-software company. I want you to use your GUI's full design and deployment capability on it — treat this as a real client project, not a quick pass.

**What's included:** 6 pages (`index.html`, `projectpulse.html`, `baseline-review.html`, `coming-soon.html`, `about.html`, `contact.html`), a shared `assets/styles.css` and `assets/script.js`. The design direction is an "engineering drawing sheet" theme — title blocks, dimension-line dividers, a blueprint grid background, monospace data labels — built for an audience of Primavera P6 planning engineers. Keep this direction; don't replace it with a generic template.

**What I want you to do:**

1. **Elevate the visual execution using your GUI's full capability** — refined spacing and type rhythm, considered micro-interactions (hover states, scroll reveals, button feedback), and any imagery/iconography that fits the engineering-drawing direction. Push the polish further than a static AI-generated first pass typically goes — this should look like a funded SaaS product's marketing site, not a template. Keep it fast-loading and keep `prefers-reduced-motion` respected for any animation you add.
2. **Do not change the copy, pricing, or links** — all product descriptions, prices, feature comparisons, and Gumroad URLs are final and already accurate. Google Analytics is already wired in with a live Measurement ID (`G-45PFV7MNN1`) — do not modify, remove, or regenerate that snippet. Preserve every HTML comment that says `REPLACE_WITH_...` exactly as-is (Microsoft Store URLs, the Formspree form ID) — do not invent values for them or remove the comments. Also preserve every `data-track`, `data-destination`, and `data-tool` attribute on buttons/links exactly as-is — they're wired to analytics events and must survive any markup changes you make.
3. **Keep it a static site** — no backend, no build step, no dependencies beyond what's already linked (Google Fonts via CDN). It needs to run as plain files on GitHub Pages.
4. **Deploy it to GitHub Pages** using your GUI's GitHub integration: create a new repository named exactly `Projects-Control` under the GitHub account `mdfarooque2010`, push these files preserving the `assets/` folder structure, enable Pages from the `main` branch root, and confirm the live URL is `https://mdfarooque2010.github.io/Projects-Control/` — this exact URL is already registered in Google Analytics, so it must match precisely.
5. **Verify before handing back:** every nav link works on every page, both Gumroad buttons open the correct listing, the site is fully usable on a mobile viewport (375px wide) and a desktop viewport, and there are no console errors.
6. **Tell me explicitly** what you changed design-wise and list every remaining placeholder I still need to fill in (Microsoft Store links, support form ID, anything else).
