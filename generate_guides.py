# -*- coding: utf-8 -*-
"""Generate long-tail SEO guide pages using the shared Schedulytics site chrome.
Each guide targets a winnable informational query and funnels to a product page.
Run:  python generate_guides.py
"""
import json, io, os

BASE = "https://schedulytics.app/"

HEAD = """<!doctype html>
<html lang="en">
<head>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','GTM-M5MRZWPH');</script>
<!-- End Google Tag Manager -->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="{url}">

<!-- Open Graph -->
<meta property="og:type" content="article">
<meta property="og:site_name" content="Schedulytics">
<meta property="og:title" content="{ogtitle}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://schedulytics.app/assets/screenshots/progress/html_dashboard.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{ogtitle}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://schedulytics.app/assets/screenshots/progress/html_dashboard.png">

<!-- Fonts & Stylesheet -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700;800&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">

<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-45PFV7MNN1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-45PFV7MNN1');
</script>

<!-- Structured Data / JSON-LD -->
<script type="application/ld+json">
{jsonld}
</script>
</head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-M5MRZWPH"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<!-- FULL-BLEED CELEBRATION HEADER -->
<div class="promo-banner promo-independence">
  <canvas id="celebration-canvas"></canvas>
  <div class="celebration-banner-inner">
    <div class="celebration-left">
      <img src="assets/branding/indian-flag-emblem.svg" alt="Indian National Flag" class="top-flag-emblem">
      <div class="celebration-title-group">
        <span class="celebration-main-title">Celebrating India's 80th Independence Day</span>
        <span class="celebration-sub-title">Special Independence Festival Offer &middot; Flat 75% OFF All Schedulytics Tools</span>
      </div>
    </div>
    <div class="celebration-right">
      <img src="assets/branding/indian-rosette.svg" alt="Ashoka Chakra Rosette Emblem" class="top-greeting-rosette-img">
      <span class="celebration-badge-pill">&#11088; 75% OFF SPECIAL</span>
      <span class="celebration-timer-tag" id="offer-countdown" data-deadline="2026-09-20T23:59:59+03:00">
        Ends 20 September 2026
      </span>
    </div>
  </div>
</div>

<header class="site-header">
  <div class="wrap">
    <div class="brand">
      <a href="index.html" class="wordmark">Schedulytics</a>
      <span class="tagline">Schedule Analytics for Primavera P6</span>
    </div>
    <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">MENU</button>
    <nav class="nav">
      <a href="index.html" class="nav-home">Home</a>
      <a href="progress-schedulytics.html" class="nav-progress">Progress Schedulytics</a>
      <a href="baseline-schedulytics.html" class="nav-baseline">Baseline Schedulytics</a>
      <a href="coming-soon.html" class="nav-soon">Coming Soon</a>
      <a href="about.html" class="nav-about">About</a>
      <a href="contact.html" class="nav-contact">Contact</a>
    </nav>
  </div>
</header>

<section class="hero" style="padding: 48px 0 24px;">
  <div class="wrap">
    <span class="eyebrow">{eyebrow}</span>
    <h1 style="font-size: clamp(2rem, 3.6vw, 3rem); max-width: 26ch; line-height: 1.15; margin: 8px 0 14px;">{h1}</h1>
    <p style="max-width: 64ch; color: var(--ink-faint); font-size: 1.05rem;">{intro}</p>
  </div>
</section>

<section class="section reveal-on-scroll" style="border-top:none; padding-top:0;">
  <div class="wrap">
    <article class="panel" style="max-width:74ch;">
{body}
{related}
    </article>
  </div>
</section>

<footer class="site-footer">
  <div class="wrap">
    <p class="footer-legal">&copy; 2026 Mohammed Farooque. All rights reserved. Independently developed. Not affiliated with, endorsed by, or sponsored by Oracle Corporation or Primavera. "P6" and "Primavera" are trademarks of Oracle Corporation, referenced here only to describe compatibility.</p>
    <nav class="footer-nav">
      <a href="index.html">Home</a>
      <a href="contact.html">Contact</a>
      <a href="privacy.html">Privacy</a>
      <a href="terms.html">Terms</a>
    </nav>
  </div>
</footer>

<script src="assets/script.js"></script>
</body>
</html>
"""

CTA = """
      <div class="panel" style="background: var(--wash, #f1f5f9); margin: 28px 0; padding: 22px;">
        <h3 style="margin-top:0;">{cta_title}</h3>
        <p style="margin-bottom:16px;">{cta_text}</p>
        <a class="btn btn-primary" href="{cta_href}" data-track="cta_click" data-tool="{slug}">{cta_btn}</a>
      </div>
"""

def breadcrumb(name, url):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": name, "item": url},
        ],
    }

def article_node(headline, desc, url):
    return {
        "@type": "Article",
        "headline": headline,
        "description": desc,
        "author": {"@type": "Person", "name": "Mohammed Farooque"},
        "publisher": {"@type": "Organization", "name": "Schedulytics", "url": BASE},
        "mainEntityOfPage": url,
        "datePublished": "2026-08-19",
        "dateModified": "2026-08-19",
    }

def faq_node(pairs):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in pairs
        ],
    }

GUIDES = []

# ---------------------------------------------------------------------------
# GUIDE 2 — DCMA 14-Point Assessment checklist
# ---------------------------------------------------------------------------
GUIDES.append(dict(
    slug="guide-dcma-14-point-assessment-checklist",
    title="DCMA 14-Point Assessment Checklist Explained (2026 Guide) | Schedulytics",
    ogtitle="DCMA 14-Point Assessment Checklist Explained",
    desc="A plain-English breakdown of all 14 DCMA schedule checks, their pass/fail thresholds, and how to run the full assessment on a Primavera P6 schedule offline.",
    keywords="DCMA 14-point assessment, DCMA 14 point checklist, DCMA schedule metrics thresholds, P6 schedule health check, baseline schedule audit, schedule quality analysis",
    eyebrow="Schedule Quality Guide",
    h1="The DCMA 14-Point Assessment Checklist, Explained",
    intro="The 14 checks the U.S. Defense Contract Management Agency uses to judge whether a schedule is trustworthy — each metric, its threshold, what a failure really means, and how to run the whole assessment on a P6 file in seconds.",
    cta_title="Run all 14 checks automatically",
    cta_text="Baseline Schedulytics audits a P6 .xer against the DCMA 14-point and 22-point criteria and exports a pass/fail scorecard with a Word narrative — 100% offline.",
    cta_href="baseline-schedulytics.html",
    cta_btn="See Baseline Schedulytics →",
    body="""
      <h2>What is the DCMA 14-Point Assessment?</h2>
      <p>The <strong>DCMA 14-Point Assessment</strong> is a set of 14 objective checks developed by the U.S. Defense Contract Management Agency to measure the structural quality of a project schedule. It does not judge whether the dates are <em>realistic</em> — it judges whether the schedule is <em>built correctly</em> enough to be believed. A schedule that fails these checks cannot reliably calculate a critical path, so its forecast dates and any delay analysis built on it are suspect.</p>
      <p>It is the de-facto industry standard for baseline acceptance on EPC, oil &amp; gas, defence and infrastructure projects worldwide.</p>

      <h2>The 14 checks and their thresholds</h2>
      <ol>
        <li><strong>Logic</strong> — activities missing a predecessor or successor should be under <strong>5%</strong>. Open ends break the critical path.</li>
        <li><strong>Leads (negative lag)</strong> — target <strong>0%</strong>. Negative lag distorts the forward pass and hides float.</li>
        <li><strong>Lags</strong> — relationships with positive lag should be under <strong>5%</strong>. Excessive lag hides missing activities.</li>
        <li><strong>Relationship Types</strong> — at least <strong>90%</strong> should be Finish-to-Start. Too many SS/FF pairs signal manipulated logic.</li>
        <li><strong>Hard Constraints</strong> — under <strong>5%</strong>. Mandatory dates override logic and freeze the critical path.</li>
        <li><strong>High Float</strong> — activities with total float over 44 working days should be under <strong>5%</strong>. Usually a symptom of missing logic.</li>
        <li><strong>Negative Float</strong> — target <strong>0%</strong>. Any negative float means the schedule cannot meet a deadline as logically built.</li>
        <li><strong>High Duration</strong> — activities longer than 44 working days should be under <strong>5%</strong>. Long tasks hide progress and risk.</li>
        <li><strong>Invalid Dates</strong> — no actual dates in the future, no forecast dates in the past relative to the data date.</li>
        <li><strong>Resources</strong> — every activity with duration should carry cost or resource loading (where the schedule is resource-loaded).</li>
        <li><strong>Missed Tasks</strong> — under <strong>5%</strong> of baseline tasks should have slipped past their baseline finish.</li>
        <li><strong>Critical Path Test</strong> — inserting a large deliberate delay on a critical activity must push the project finish. If it doesn't, the critical path is broken.</li>
        <li><strong>Critical Path Length Index (CPLI)</strong> — should be <strong>&ge; 0.95</strong>. Measures how efficiently the critical path uses remaining time.</li>
        <li><strong>Baseline Execution Index (BEI)</strong> — should be <strong>&ge; 0.95</strong>. The ratio of tasks completed to tasks that should have been completed.</li>
      </ol>

      <h2>How to read the results</h2>
      <p>Any single failure is a conversation, not a rejection — but a cluster of failures in <em>Logic, Leads, Constraints and Negative Float</em> together means the critical path is not trustworthy, and every downstream forecast is built on sand. That is exactly the pattern reviewers look for when they reject a baseline submittal.</p>

      <h2>Running the assessment on a P6 schedule</h2>
      <p>You can compute each metric by hand with P6 layouts and filters, but on a 2,000-activity schedule that is hours of work and easy to get wrong. <a href="baseline-schedulytics.html">Baseline Schedulytics</a> reads the .xer or .xml directly and produces the full 14-point (and extended 22-point) scorecard with pass/fail status, calculated percentages, a Monte Carlo confidence band, and a clean Word narrative — offline, in seconds.</p>
""",
    faq=[
        ("What is a good DCMA 14-point score?",
         "There is no single score — the assessment is 14 separate pass/fail checks against thresholds (most at under 5%, with Leads and Negative Float at 0%, and CPLI and BEI at 0.95 or above). A healthy baseline passes all or nearly all of them; failures in Logic, Constraints and Negative Float together are the most serious."),
        ("Does Primavera P6 run the DCMA check natively?",
         "P6 Professional includes a Check Schedule report that covers most, but not all, DCMA metrics — it omits Missed Tasks, the Critical Path Test, CPLI and BEI. A dedicated tool is needed for the complete 14-point assessment."),
        ("Is the DCMA 14-point assessment only for defence projects?",
         "No. Although it originated with the U.S. Defense Contract Management Agency, it is now used as a general schedule-quality standard across EPC, oil & gas, construction and infrastructure projects globally."),
    ],
    breadcrumb_name="DCMA 14-Point Checklist",
))

# ---------------------------------------------------------------------------
# GUIDE 3 — Fix negative total float in P6
# ---------------------------------------------------------------------------
GUIDES.append(dict(
    slug="guide-fix-negative-total-float-p6",
    title="How to Fix Negative Total Float in Primavera P6 (Step-by-Step) | Schedulytics",
    ogtitle="How to Fix Negative Total Float in Primavera P6",
    desc="Why negative total float appears in Primavera P6 and a step-by-step method to diagnose and remove it — constraints, broken logic, and out-of-sequence progress.",
    keywords="negative total float P6, fix negative float Primavera, why is my float negative, P6 negative float causes, critical path negative float, total float troubleshooting",
    eyebrow="Primavera P6 Troubleshooting",
    h1="How to Fix Negative Total Float in Primavera P6",
    intro="Negative float means your schedule can no longer meet a deadline as logically built. Here is what actually causes it in P6, and a repeatable step-by-step method to find and remove the root cause.",
    cta_title="Find float leaks automatically",
    cta_text="Baseline Schedulytics flags negative-float chains, hard constraints and out-of-sequence logic in a single audit report — offline, straight from your .xer file.",
    cta_href="baseline-schedulytics.html",
    cta_btn="See Baseline Schedulytics →",
    body="""
      <h2>What negative total float actually means</h2>
      <p><strong>Total float</strong> is the amount of time an activity can slip without delaying the project finish (or a deadline constraint). When float goes <strong>negative</strong>, Primavera P6 is telling you the opposite: as the logic and constraints are currently built, the activity is already <em>behind</em> the date it must hit to protect the deadline. A total float of -18 means you are 18 days short.</p>
      <p>Negative float is not automatically wrong — sometimes it is a true, honest signal that you are late. The problem is that it is very often an <em>artefact</em> of a constraint or a logic error, and until you rule those out you can't trust it.</p>

      <h2>The four causes, in order of likelihood</h2>
      <h3>1. A hard constraint fighting the logic</h3>
      <p>By far the most common cause. A <em>Must Finish By</em> or <em>Finish On or Before</em> constraint sets a deadline earlier than the logic can deliver, so P6 back-propagates negative float up the driving chain. Check the affected activities and their predecessors for constraints first.</p>
      <h3>2. Out-of-sequence progress</h3>
      <p>When work is reported on an activity before its predecessor finished, the retained-logic calculation can throw negative float. Look for activities with actual starts that violate their relationships.</p>
      <h3>3. Deadline (project Must Finish By) date passed</h3>
      <p>If the project-level Must Finish By date is earlier than the calculated finish, every activity on the critical path shows negative float. This is the honest kind — you are genuinely forecasting late.</p>
      <h3>4. Broken or missing logic</h3>
      <p>Open ends and dangling activities can interact with constraints to produce misleading float values.</p>

      <h2>Step-by-step: diagnose and fix</h2>
      <ol>
        <li><strong>Isolate it.</strong> Add a filter for <code>Total Float &lt; 0</code> and sort ascending, so the most negative (the driving activity) is at the top.</li>
        <li><strong>Trace the driving chain.</strong> From the most negative activity, walk the predecessor logic backwards (Ctrl-click Goto Predecessor) to find where the negative float originates.</li>
        <li><strong>Check for constraints on that chain.</strong> Add the Primary/Secondary Constraint columns. Remove or relax any constraint that is not contractually required.</li>
        <li><strong>Check the data date and out-of-sequence progress.</strong> Re-schedule (F9) with Retained Logic and review the scheduling log for out-of-sequence relationships.</li>
        <li><strong>Re-run F9 and re-measure.</strong> If float returns to positive, the constraint or logic was the culprit. If it stays negative after constraints are clean, the delay is real — now it is a recovery / acceleration problem, not a schedule-hygiene one.</li>
      </ol>

      <h2>Doing this across many files</h2>
      <p>Tracing float by hand is fine for one schedule. Across a portfolio of contractor submittals it is slow and inconsistent. <a href="baseline-schedulytics.html">Baseline Schedulytics</a> reads each .xer, lists every negative-float activity with its driving chain and any offending constraints, and scores the schedule against DCMA criteria — so you can separate genuine delay from constraint artefacts in seconds. See the full <a href="guide-dcma-14-point-assessment-checklist.html">DCMA 14-point checklist</a> for the related checks.</p>
""",
    faq=[
        ("Is negative float always bad?",
         "No. Negative float can be an honest signal that the project is forecasting past its deadline. The problem is that it is often caused instead by a hard constraint or a logic error, so you must rule those out before treating it as real delay."),
        ("What is the most common cause of negative float in P6?",
         "A hard date constraint — such as Must Finish By or Finish On or Before — set earlier than the logic can deliver. P6 propagates the shortfall as negative float up the driving chain."),
        ("How do I remove negative float without changing the deadline?",
         "You cannot make genuine negative float disappear without either changing logic/durations (acceleration) or moving the deadline. What you can remove is artificial negative float caused by unnecessary constraints or out-of-sequence progress."),
    ],
    breadcrumb_name="Fix Negative Total Float",
))

# ---------------------------------------------------------------------------
# GUIDE 4 — FIDIC Extension of Time claim
# ---------------------------------------------------------------------------
GUIDES.append(dict(
    slug="guide-fidic-extension-of-time-claim",
    title="How to Prepare a FIDIC Extension of Time (EOT) Claim | Schedulytics",
    ogtitle="How to Prepare a FIDIC Extension of Time (EOT) Claim",
    desc="A planner's guide to building a defensible FIDIC Extension of Time claim: Clause 8.4 and 20.1 basics, notice timing, Time Impact Analysis, and the evidence you need.",
    keywords="FIDIC extension of time claim, EOT claim FIDIC 8.4, clause 20.1 notice, time impact analysis TIA, delay claim primavera P6, EOT narrative, forensic delay analysis",
    eyebrow="Claims & Delay Guide",
    h1="How to Prepare a FIDIC Extension of Time (EOT) Claim",
    intro="A practical walkthrough for planners and claims engineers: the FIDIC clauses that matter, why notice timing can sink a valid claim, how a Time Impact Analysis proves entitlement, and the evidence trail you need from P6.",
    cta_title="Build delay claims from P6 data faster",
    cta_text="Progress Schedulytics generates period-over-period variance and an automated Word & PDF delay narrative straight from your P6 updates — the factual backbone of an EOT submission.",
    cta_href="progress-schedulytics.html",
    cta_btn="See Progress Schedulytics →",
    body="""
      <h2>What an EOT claim is — and isn't</h2>
      <p>An <strong>Extension of Time (EOT)</strong> claim asks the Engineer to move the contractual Completion Date because of a delay the Contractor is not responsible for. Under the <strong>FIDIC</strong> forms it does two things: it protects the Contractor from delay damages (liquidated damages), and — where the delay is compensable — it opens the door to associated cost. An EOT is about <em>time</em>; the money follows separately.</p>
      <p>A valid EOT rests on three pillars: a qualifying <strong>cause</strong>, timely <strong>notice</strong>, and a demonstrable <strong>effect on the critical path</strong>. Miss any one and an otherwise-genuine claim can fail.</p>

      <h2>The FIDIC clauses that matter</h2>
      <ul>
        <li><strong>Clause 8.4 (1999) / 8.5 (2017) — Extension of Time for Completion:</strong> lists the grounds for entitlement (variations, exceptional weather, Employer-caused delay, unforeseeable shortages, etc.).</li>
        <li><strong>Clause 20.1 (1999) / 20.2 (2017) — Contractor's Claims:</strong> the procedure. Critically, notice must be given <strong>within 28 days</strong> of when the Contractor became aware (or should have) of the event. Under the 2017 form, late notice can bar the claim entirely (a time-bar).</li>
      </ul>
      <p class="note" style="padding:12px 16px; background:var(--wash,#f1f5f9); border-radius:8px;"><strong>The 28-day notice is the single biggest killer of valid claims.</strong> Serve notice early, in writing, even before you have quantified the impact.</p>

      <h2>Proving the delay: Time Impact Analysis</h2>
      <p>Entitlement is not enough — you must show the event actually delayed the <em>project completion</em>, not just one activity. The most widely accepted prospective method is a <strong>Time Impact Analysis (TIA)</strong>, consistent with the SCL Delay Protocol and AACE 29R-03:</p>
      <ol>
        <li>Start from the <strong>approved baseline</strong> (or the last accepted update) as the reference schedule.</li>
        <li>Insert a <strong>delay fragnet</strong> — an activity or logic tie representing the delay event — at the point in time it occurred.</li>
        <li><strong>Re-schedule</strong> and measure the shift in the contractual Completion Date. That shift, day-for-day on the critical path, is your entitlement.</li>
        <li>Address <strong>concurrency</strong> and mitigation honestly — reviewers will.</li>
      </ol>

      <h2>The evidence trail from P6</h2>
      <p>A claim lives or dies on records. You need: the approved baseline, dated progress updates spanning the event, the correspondence establishing notice, and a clear variance showing the affected activities moving. This is where disciplined period reporting pays off — <a href="progress-schedulytics.html">Progress Schedulytics</a> compares consecutive P6 updates and produces an automated variance and delay narrative in Word &amp; PDF, giving you the factual chronology that underpins the TIA. For the forensic methods behind retrospective claims, see the tools on our <a href="coming-soon.html">roadmap</a>.</p>
""",
    faq=[
        ("How long do I have to give notice of an EOT under FIDIC?",
         "Under FIDIC Clause 20.1 (1999) and 20.2 (2017), the Contractor must give notice within 28 days of becoming aware, or when it should have become aware, of the delaying event. Under the 2017 form, failing to give timely notice can bar the claim entirely."),
        ("What is the difference between an EOT and a delay claim for money?",
         "An EOT is a claim for additional time to complete, which protects against delay damages. A monetary claim for prolongation cost is separate — an EOT for a compensable delay is usually a precondition for it, but time and cost are assessed independently."),
        ("Which delay analysis method should I use for an EOT?",
         "For a prospective, near-real-time assessment, Time Impact Analysis (TIA) is the most widely accepted method and aligns with the SCL Delay Protocol and AACE 29R-03. The right method also depends on the available records and the contract."),
    ],
    breadcrumb_name="FIDIC Extension of Time Claim",
))

# ---------------------------------------------------------------------------
# GUIDE 5 — Build an S-curve in Excel from P6
# ---------------------------------------------------------------------------
GUIDES.append(dict(
    slug="guide-p6-s-curve-excel",
    title="How to Build an S-Curve in Excel from Primavera P6 | Schedulytics",
    ogtitle="How to Build an S-Curve in Excel from Primavera P6",
    desc="Step-by-step: export planned and actual progress from Primavera P6 and build a cumulative planned vs. actual S-curve in Excel — or generate it automatically.",
    keywords="P6 S-curve Excel, how to make an S-curve in Excel, planned vs actual S-curve, cumulative progress curve P6, primavera S-curve, project progress S curve",
    eyebrow="Reporting How-To",
    h1="How to Build an S-Curve in Excel from Primavera P6",
    intro="The planned-vs-actual S-curve is the single most-requested progress chart on any project. Here is how to build one properly from P6 data in Excel — and how to skip the manual work entirely.",
    cta_title="Get S-curves generated for you",
    cta_text="Progress Schedulytics builds cumulative planned-vs-actual S-curves (and 21 other analytics sheets) straight from a P6 XML export — no manual pivot tables.",
    cta_href="progress-schedulytics.html",
    cta_btn="See Progress Schedulytics →",
    body="""
      <h2>What an S-curve shows</h2>
      <p>An <strong>S-curve</strong> plots <em>cumulative</em> progress over time — typically planned value against actual (earned) value. It gets its name from its shape: slow at the start (mobilisation), steep through the middle (peak execution), and flattening at the end (commissioning and close-out). The gap between the planned and actual curves is your schedule performance at a glance.</p>

      <h2>Step-by-step in Excel</h2>
      <ol>
        <li><strong>Decide the measure.</strong> Progress can be weighted by cost (budgeted total cost), by labour hours, or by activity count. Cost-weighted is the most common and the most meaningful.</li>
        <li><strong>Export from P6.</strong> Export the activity list with Budgeted Total Cost, Baseline Start/Finish (for planned) and Actual/Remaining dates and % complete (for actual). An XML or XER export carries all of this.</li>
        <li><strong>Spread the value over time.</strong> For each activity, distribute its value across the periods (weeks or months) between its start and finish. A simple linear spread is fine for most reporting; front/back-loaded spreads are more accurate but more work.</li>
        <li><strong>Build a period table.</strong> Create a column of month-ending dates. For each period, sum the planned value that falls in it, and separately the earned value.</li>
        <li><strong>Make it cumulative.</strong> Add running-total columns for both planned and earned — these are your two curves.</li>
        <li><strong>Chart it.</strong> Insert a 2-D line chart with the period dates on the X axis and cumulative planned and cumulative earned as two series. Add data labels and a data-date marker.</li>
      </ol>

      <h2>The catch</h2>
      <p>Doing this by hand is a few hours of pivot tables every reporting cycle, and it breaks the moment the schedule is re-baselined or activities are added. Every planner has rebuilt the same S-curve a hundred times.</p>

      <h2>The automated route</h2>
      <p><a href="progress-schedulytics.html">Progress Schedulytics</a> reads the P6 XML export and produces the cumulative planned-vs-actual S-curve automatically, inside a 22-sheet Excel workbook that also includes WBS breakdowns, SPI/CPI trends and float analysis — 100% offline. If you also need the underlying data in Excel first, see our guide on <a href="guide-convert-p6-xer-to-excel.html">converting a P6 XER file to Excel</a>.</p>
""",
    faq=[
        ("What data do I need from P6 to build an S-curve?",
         "At minimum: each activity's weighting value (budgeted cost, hours or count), its planned (baseline) start and finish for the planned curve, and its actual dates and percent complete for the actual/earned curve. An XER or XML export contains all of this."),
        ("Should an S-curve be based on cost or on progress percentage?",
         "Cost-weighted (or hours-weighted) S-curves are the most meaningful because they reflect where the real effort and value sit. A simple activity-count curve treats a one-day task the same as a three-month one, which distorts the picture."),
        ("Can I generate a P6 S-curve without building it manually in Excel?",
         "Yes. Tools such as Progress Schedulytics read the P6 export and generate the cumulative planned-vs-actual S-curve automatically as part of a multi-sheet Excel analytics workbook, removing the manual pivot-table work each cycle."),
    ],
    breadcrumb_name="Build a P6 S-Curve in Excel",
))

# ---------------------------------------------------------------------------
# Related-guides cross-link block
# ---------------------------------------------------------------------------
ALL_LINKS = [
    ("guide-convert-p6-xer-to-excel.html", "How to Convert a P6 XER File to Excel"),
    ("guide-dcma-14-point-assessment-checklist.html", "The DCMA 14-Point Assessment Checklist"),
    ("guide-fix-negative-total-float-p6.html", "How to Fix Negative Total Float in P6"),
    ("guide-fidic-extension-of-time-claim.html", "How to Prepare a FIDIC EOT Claim"),
    ("guide-p6-s-curve-excel.html", "How to Build an S-Curve in Excel from P6"),
]

def related_block(current_slug):
    items = [f'        <li><a href="{href}">{label}</a></li>'
             for href, label in ALL_LINKS if not href.startswith(current_slug)]
    return ("""
      <h2 style="margin-top:34px;">Related planning guides</h2>
      <ul>
""" + "\n".join(items) + "\n      </ul>")

def build(g):
    url = BASE + g["slug"] + ".html"
    graph = [breadcrumb(g["breadcrumb_name"], url),
             article_node(g["ogtitle"], g["desc"], url),
             faq_node(g["faq"])]
    jsonld = json.dumps({"@context": "https://schema.org", "@graph": graph},
                        indent=2, ensure_ascii=False)
    body = g["body"] + CTA.format(cta_title=g["cta_title"], cta_text=g["cta_text"],
                                  cta_href=g["cta_href"], cta_btn=g["cta_btn"], slug=g["slug"])
    html = HEAD.format(title=g["title"], desc=g["desc"], keywords=g["keywords"], url=url,
                       ogtitle=g["ogtitle"], eyebrow=g["eyebrow"], h1=g["h1"],
                       intro=g["intro"], jsonld=jsonld, body=body,
                       related=related_block(g["slug"]))
    out = g["slug"] + ".html"
    with io.open(out, "w", encoding="utf-8") as f:
        f.write(html)
    # validate JSON-LD
    json.loads(jsonld)
    print("wrote", out, "(%d bytes)" % len(html.encode("utf-8")))

if __name__ == "__main__":
    for g in GUIDES:
        build(g)
    print("done:", len(GUIDES), "guides")
