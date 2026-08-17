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

## Current Deployment State & Checklist

- ✅ **Live Custom Domain:** Deployed at `https://schedulytics.app/` via GitHub Pages with CNAME and HTTPS enforcement.
- ✅ **Google Analytics 4 & Tag Manager:** Measurement ID `G-45PFV7MNN1` and GTM container `GTM-M5MRZWPH` are active across all pages.
- ✅ **Microsoft Store Links are LIVE:**
  - Progress Schedulytics: `https://apps.microsoft.com/detail/9PJR22LWZFJ0` (App ID: `9PJR22LWZFJ0`)
  - Baseline Schedulytics: `https://apps.microsoft.com/detail/9PHV1LFVJ70J` (App ID: `9PHV1LFVJ70J`)
- ✅ **Gumroad Licensing & 2-Step Buy Flow:**
  - Progress Schedulytics: `https://mdfarooque2010.gumroad.com/l/ProjectPulse`
  - Baseline Schedulytics: `https://mdfarooque2010.gumroad.com/l/baseline-review-intelligence`
  - 2-Step funnel pages live at `/buy/progress/` and `/buy/baseline/`
- ✅ **Walkthrough Video:** Embedded in `progress-schedulytics.html` from `assets/p6-progress-dashboard.mp4`.
- ✅ **Contact Information:** Email `md.farooque@gmail.com` and phone `+91 92627 46271` active.
- **Formspree Notification Form:** Create a free form at [formspree.io](https://formspree.io/) and replace `REPLACE_WITH_YOUR_FORM_ID` in `contact.html` whenever ready.

## Updating Content Later

- Every page is a plain `.html` file.
- Pages: `index.html`, `progress-schedulytics.html`, `baseline-schedulytics.html`, `coming-soon.html`, `about.html`, `contact.html`, `privacy.html`, `terms.html`.
- After editing, commit and push to `main` branch — GitHub Pages redeploys automatically within 1–2 minutes.

## Adding a New Product Page Later

- Duplicate `progress-schedulytics.html` or `baseline-schedulytics.html` as a template.
- Add the link to the `<nav>` block in the header and footer of every page.
