# Running schedulytics.app yourself

You do not need a developer, a subscription, or any software installed to change
the text on this site. Everything here can be done from a web browser in about a
minute.

---

## 1. How the site actually works

```
You edit a file on GitHub  →  GitHub Pages rebuilds  →  schedulytics.app updates
        (30 seconds)              (about 1 minute)            (live)
```

There is no database and no login panel to break. The site *is* these files. If a
file says `$49.50`, the page says `$49.50`. Change the file, change the page.

---

## 2. Making a change (the only procedure you need)

1. Go to **https://github.com/mdfarooque2010/Projects-Control**
2. Click the file you want to change — for example `index.html`
3. Click the **pencil icon** (✏️) at the top right — this opens the editor
4. Use **Ctrl+F** to find the text you want to change
5. Change **only the words**, never the `<angle brackets>` around them
6. Click the **Preview** tab to check nothing looks broken
7. Scroll down, type a short note like `update launch price`, click
   **Commit changes**
8. Wait about a minute, then reload schedulytics.app

**If something goes wrong:** click **History** at the top of the file, open the
previous version, and click **Revert**. Nothing is ever permanently lost — every
version is kept.

---

## 3. Where the things you'll change most often live

| What you want to change | File | Search for |
|---|---|---|
| The two discount percentages | `index.html` | `step-pct` |
| The offer deadline ("end of August 2026") | `index.html` | `offer-until` |
| The Android pre-launch note | `index.html` | `teaser` |
| Product prices on the home page | `index.html` | `price-was` |
| Current version number (v3.0.0) | `index.html` | `Current release` |
| "Available now" / "Coming next" feature lists | `index.html` | `tick-list` |
| Headline on the home page | `index.html` | `<h1>` |
| Progress Schedulytics product page | `progress-schedulytics.html` | — |
| Baseline Schedulytics product page | `baseline-schedulytics.html` | — |
| Upcoming tools | `coming-soon.html` | — |
| Your bio | `about.html` | — |
| Email / WhatsApp number | `contact.html` | `mailto:` |
| Privacy policy | `privacy.html` | — |
| Colours, fonts, spacing | `assets/styles.css` | see section 5 |

Blocks that are safe and expected to be edited are marked in the HTML like this:

```html
<!-- ═══════════════════════════════════════════════════════
     EDITABLE — LAUNCH OFFER
       the two percentages   -> search for  step-pct
       the deadline          -> search for  offer-until
     ═══════════════════════════════════════════════════════ -->
```

---

## 4. The three rules that keep you out of trouble

1. **Edit between the brackets, not the brackets.**
   In `<strong>$49.50</strong>` you may change `$49.50` freely.
   Do not touch `<strong>` or `</strong>`.

2. **Keep tags in pairs.** Every `<p>` needs its `</p>`. If you delete an opening
   tag you must delete its closing tag too.

3. **Use the Preview tab before committing.** It catches almost every mistake.

Special characters, if you need them: `&amp;` = &, `&rarr;` = →, `&mdash;` = —.

---

## 5. Changing colours

Open `assets/styles.css`. The first block sets every colour on the site:

```css
:root {
  --paper:  #f5f6f2;   /* page background      */
  --ink:    #16223e;   /* main text, borders   */
  --accent: #d4601c;   /* orange - buttons     */
  --live:   #2f6f4e;   /* green  - "Live"      */
  --night:  #101a2e;   /* dark section bands   */
}
```

Change one value and it updates everywhere on the site at once. This is the safest
file to experiment in — colour mistakes look wrong but never break the page.

---

## 6. If you ever want a proper admin panel

Editing HTML works, but if you'd rather fill in a form than find text in a file,
you can add a free CMS on top of these same files:

- **Sveltia CMS** or **Decap CMS** — adds an admin screen at
  `schedulytics.app/admin`. You log in with your GitHub account, edit content in
  form fields, click Save, and it commits the change for you. Free, and it does not
  replace anything — the site keeps working exactly as it does now.

This is a half-day of setup and is worth doing only if you find yourself editing
often. The GitHub method above costs nothing and has no moving parts.

---

## 7. What you should NOT change without checking

| File | Why |
|---|---|
| `CNAME` | Contains `schedulytics.app`. Deleting it takes the domain off the site. |
| The Google Analytics / Tag Manager `<script>` blocks | Removing them loses your visitor statistics. |
| The footer trademark line | It is deliberate legal wording about Oracle and Primavera. |
| `assets/script.js` | Handles the mobile menu and scroll effects. |

---

## 8. Emergency: the site is broken

1. Go to the repository → **commits** (the clock icon)
2. Find the last commit that worked
3. Click it, then **Revert**
4. The site is back within a minute

You cannot permanently break this site. Every version is stored forever.
