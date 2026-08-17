# Analytics Guide — where to find every number you asked about

GitHub Pages has no server or database, so a custom login-protected admin
panel isn't possible here without adding real backend infrastructure. What
the site *does* include is full tracking wired into **Google Analytics 4**
(free) — which already answers everything on your list except confirmed
purchases, which live in Gumroad's and Microsoft's own dashboards (better
sources than anything we'd rebuild).

## One-time setup (~5 minutes)

1. Go to [analytics.google.com](https://analytics.google.com) → Admin → Create a property (e.g. "Projects-Control").
2. Add a **Web** data stream, enter your site's URL.
3. Copy the **Measurement ID** — looks like `G-ABC1234XYZ`.
4. Open every `.html` file in this site and replace both occurrences of
   `G-XXXXXXXXXX` with your real ID. (Fastest way: find-and-replace across
   all files in any text editor, or ask me to do it once you have the ID.)
5. Publish the site, visit it yourself, then check **Reports → Realtime**
   in GA4 — you should see your own visit within a minute.

## Where to find what you asked for

| You asked for | Where it is in GA4 |
|---|---|
| How many visits | **Reports → Life cycle → Engagement → Overview** — total users/sessions |
| Country-wise visits | **Reports → User → Demographics → Country** |
| Weekly / monthly / yearly trends | Top-right date picker on any report — switch range, or use **Reports → Engagement → Overview** with a custom comparison |
| Which tool gets visited more | **Reports → Engagement → Pages and screens** — sort by views; compare `/progress-schedulytics.html` vs `/baseline-schedulytics.html` vs `/coming-soon.html` |
| Did they try to visit Gumroad / Microsoft Store | **Reports → Engagement → Events**, filter for `outbound_click` — each event carries a `destination` (gumroad / microsoft_store) and `tool` parameter so you can break it down either way |
| Which tool people click "buy" on more | Same `outbound_click` event, group by the `tool` parameter |
| Interest in unreleased tools | **Events**, filter for `interest_click` — fires when someone clicks "Notify me at launch" on the Coming Soon page, tagged by tool |
| Actual purchases / downloads | **Not in GA4** — check these instead: |

### Actual sales and installs (better tracked at the source)

- **Gumroad sales**: log into gumroad.com → your dashboard already shows every sale, revenue, and location, per product, with no setup needed.
- **Microsoft Store installs**: [Partner Center](https://partner.microsoft.com) → your app → Analytics tab shows acquisitions, installs, and usage per app natively.

Combining these two with the `outbound_click` GA4 events gives you a real
funnel: **site visit → clicked buy → confirmed sale**, just split across two
free dashboards instead of one.

## Optional next step (not built yet — needs a decision first)

If you eventually want Gumroad sales to show up automatically inside GA4
itself (true "purchase" events, not just clicks), that requires Gumroad's
webhook feature posting to a small serverless function (e.g. a free
Cloudflare Worker) that forwards the event to GA4's Measurement Protocol.
This needs a backend, however minimal, which is a bigger step than the rest
of this site — happy to build it whenever you're ready to add it, since it's
a separate, contained piece of infrastructure.
