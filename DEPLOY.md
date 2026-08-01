# Deploying this site with GitHub Pages

You already plan to create a GitHub account for CivilCalc Pro — use the same account here.

## First-time setup (~10 minutes)

1. **Create a repository**
   - Go to github.com → New repository
   - Name it exactly `Projects-Control` (this matches the site URL already set up in Google Analytics)
   - Keep it **Public** (required for free GitHub Pages) or use Pages with a private repo if you're on GitHub Pro
   - Don't initialize with a README (you already have these files)

2. **Upload the files**
   - Easiest way with no command line: on the new repo page, click **"uploading an existing file"**
   - Drag in everything from this folder, **keeping the `assets/` folder structure intact**
   - Commit directly to the `main` branch

3. **Turn on Pages**
   - In the repo, go to **Settings → Pages**
   - Under "Build and deployment," set **Source** to `Deploy from a branch`
   - Set **Branch** to `main`, folder `/ (root)`
   - Click **Save**
   - GitHub gives you a live URL within a minute or two:
     `https://mdfarooque2010.github.io/Projects-Control/`
   - This is already the exact URL entered in your Google Analytics 4 property, so no need to go back and edit it there once you're live

4. **Test it**
   - Open the URL, click through every nav link
   - Click both Gumroad buy buttons and confirm they go to the right listings
   - Check the site on your phone (resize your browser or use your phone directly)

## Before you go further

- ✅ **Google Analytics 4 is already set up** — Measurement ID `G-45PFV7MNN1` is live in all 6 pages. Once the site is deployed and gets its first visit, check **Realtime** in GA4 to confirm it's tracking.
- **Microsoft Store links are placeholders.** Both `projectpulse.html` and `baseline-review.html` have two spots each (`REPLACE_WITH_PROJECTPULSE_APP_ID` / `REPLACE_WITH_PBL_APP_ID`) — search-replace these with your real `apps.microsoft.com/detail/...` URLs once you have them, or send them to me and I'll patch the files.
- **Add real screenshots and a walkthrough video** when ready — see `assets/screenshots/README.md` and the HTML comments above each screenshot grid / video slot in `projectpulse.html` and `baseline-review.html` for the exact swap-in snippet.
- **Confirm the "was" prices.** The 50%-off display assumes the discount is exactly half (ProjectPulse: was $99, now $49.50 · Baseline Review: was $79, now $39.50). If your actual regular price differs, update the `price-was` and `price-now` values in both product pages.
- **Wire up the "notify me" form**: create a free form at formspree.io, then paste the form action URL into `contact.html` where it says `REPLACE_WITH_YOUR_FORM_ID`. Takes about 2 minutes and needs no code.
- Contact details (email + phone) are already filled in with your real ones.
- **Custom domain (optional, do before running paid ads)**: GitHub Pages supports this directly.
  1. Buy a domain from any registrar.
  2. In the repo, go to **Settings → Pages → Custom domain**, enter your domain, save. GitHub creates a `CNAME` file in your repo automatically.
  3. At your domain registrar, add the DNS records GitHub shows you (usually an `A` record set for the apex domain, or a `CNAME` record for a `www` subdomain pointing to `your-username.github.io`).
  4. Allow up to 24–48 hours for DNS to propagate. Check "Enforce HTTPS" once it's verified.

## Updating content later (v3.0.0 / v4.0.0, new pricing, etc.)

- Every page is a plain `.html` file — open it in any text editor (or come back here and I'll edit it with you).
- The feature lists on `projectpulse.html` and `baseline-review.html` are marked with an inline `.notice` callout box flagging what's pending an update — search for "Note:" or "next update" in each file to find the exact spot to revise.
- After editing, just re-upload the changed file to the same GitHub repo (or commit via git if you're comfortable with it) — Pages redeploys automatically within a minute or two.

## Adding a new product page later

- Duplicate `projectpulse.html` or `baseline-review.html` as a starting template — they already have the title-block, feature-list, and pricing panel structure.
- Add a link to it in the `<nav>` block at the top of **every** page (copy-paste is fine, there's no shared template file since this is plain HTML — six small edits).
