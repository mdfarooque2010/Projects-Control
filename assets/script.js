/**
 * Schedulytics — Interactive Client Scripts
 * Includes: Champagne & Sparkle Particle Engine, FAQ Accordion, GA4 Tracker, Navigation Toggle, and Countdown Timer.
 */

document.addEventListener("DOMContentLoaded", function () {
  // ------------------------------------------------------------- 1. Navigation Toggle
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var isOpen = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
  }

  // ------------------------------------------------------------- 2. Scroll Reveal Observer
  var revealElements = document.querySelectorAll(".reveal-on-scroll");
  if (revealElements.length > 0 && typeof IntersectionObserver !== "undefined") {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("revealed");
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.05,
      rootMargin: "0px 0px -20px 0px"
    });
    revealElements.forEach(function (el) {
      observer.observe(el);
    });
  } else {
    revealElements.forEach(function (el) {
      el.classList.add("revealed");
    });
  }

  // ------------------------------------------------------------- 3. Champagne Sparkles / Particle Fountain
  var canvas = document.getElementById("celebration-canvas");
  if (canvas && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var ctx = canvas.getContext("2d");
    var particles = [];
    var maxParticles = 55;
    var colors = [
      "rgba(255, 215, 0, ",   // Gold
      "rgba(255, 153, 51, ",  // Saffron
      "rgba(19, 136, 8, ",    // India Green
      "rgba(255, 255, 255, ", // Sparkle White
      "rgba(0, 0, 128, "      // Royal Navy
    ];

    function resizeCanvas() {
      if (canvas.parentElement) {
        canvas.width = canvas.parentElement.offsetWidth;
        canvas.height = canvas.parentElement.offsetHeight;
      }
    }
    resizeCanvas();
    window.addEventListener("resize", resizeCanvas);

    function createParticle() {
      var colorBase = colors[Math.floor(Math.random() * colors.length)];
      return {
        x: Math.random() * canvas.width,
        y: canvas.height + Math.random() * 20,
        radius: Math.random() * 2.8 + 1.2,
        colorBase: colorBase,
        alpha: Math.random() * 0.7 + 0.3,
        speedY: Math.random() * 1.2 + 0.6,
        speedX: (Math.random() - 0.5) * 0.8,
        swayAngle: Math.random() * Math.PI * 2,
        swaySpeed: Math.random() * 0.04 + 0.02,
        twinkleSpeed: Math.random() * 0.05 + 0.02,
        isStar: Math.random() > 0.65
      };
    }

    for (var i = 0; i < maxParticles; i++) {
      var p = createParticle();
      p.y = Math.random() * canvas.height; // Distribute initially
      particles.push(p);
    }

    function drawStar(ctx, cx, cy, spikes, outerRadius, innerRadius, color) {
      var rot = Math.PI / 2 * 3;
      var x = cx;
      var y = cy;
      var step = Math.PI / spikes;

      ctx.beginPath();
      ctx.moveTo(cx, cy - outerRadius);
      for (var i = 0; i < spikes; i++) {
        x = cx + Math.cos(rot) * outerRadius;
        y = cy + Math.sin(rot) * outerRadius;
        ctx.lineTo(x, y);
        rot += step;

        x = cx + Math.cos(rot) * innerRadius;
        y = cy + Math.sin(rot) * innerRadius;
        ctx.lineTo(x, y);
        rot += step;
      }
      ctx.lineTo(cx, cy - outerRadius);
      ctx.closePath();
      ctx.fillStyle = color;
      ctx.fill();
    }

    function animateSparkles() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      for (var j = 0; j < particles.length; j++) {
        var p = particles[j];
        p.y -= p.speedY;
        p.swayAngle += p.swaySpeed;
        p.x += Math.sin(p.swayAngle) * 0.5 + p.speedX;
        p.alpha += Math.sin(p.swayAngle * 2) * p.twinkleSpeed;
        var currentAlpha = Math.max(0.1, Math.min(0.95, p.alpha));

        var fillColor = p.colorBase + currentAlpha + ")";

        if (p.isStar) {
          drawStar(ctx, p.x, p.y, 4, p.radius * 2, p.radius * 0.8, fillColor);
        } else {
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
          ctx.fillStyle = fillColor;
          ctx.shadowBlur = p.radius * 3;
          ctx.shadowColor = fillColor;
          ctx.fill();
          ctx.shadowBlur = 0;
        }

        // Reset if float out of top or bounds
        if (p.y < -15 || p.x < -20 || p.x > canvas.width + 20) {
          particles[j] = createParticle();
        }
      }

      requestAnimationFrame(animateSparkles);
    }
    animateSparkles();
  }

  // ------------------------------------------------------------- 4. Interactive FAQ Accordion
  var faqQuestions = document.querySelectorAll(".faq-question");
  faqQuestions.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var item = btn.closest(".faq-item");
      var isOpen = item.classList.contains("open");

      // Optional: close other FAQ items
      document.querySelectorAll(".faq-item").forEach(function (other) {
        if (other !== item) other.classList.remove("open");
      });

      if (isOpen) {
        item.classList.remove("open");
        btn.setAttribute("aria-expanded", "false");
      } else {
        item.classList.add("open");
        btn.setAttribute("aria-expanded", "true");
      }
    });
  });

  // ------------------------------------------------------------- 5. Offer Countdown Timer
  var timerEl = document.getElementById("offer-countdown");
  if (timerEl) {
    var end = new Date(timerEl.getAttribute("data-deadline") || "2026-09-20T23:59:59+03:00");
    if (!isNaN(end)) {
      var written = end.toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" });
      function tick() {
        var ms = end - new Date();
        if (ms <= 0) {
          timerEl.textContent = "Celebration offer has ended";
          return;
        }
        var d = Math.floor(ms / 86400000),
            h = Math.floor((ms % 86400000) / 3600000),
            m = Math.floor((ms % 3600000) / 60000);
        timerEl.textContent = (d > 0 ? d + "d " + h + "h left · " : h + "h " + m + "m left · ") + "Ends " + written;
        setTimeout(tick, 60000);
      }
      tick();
    }
  }

  // ------------------------------------------------------------- 6. Google Analytics 4 Event Tracking
  document.addEventListener("click", function (e) {
    var el = e.target.closest("[data-track]");
    if (!el) return;
    if (typeof gtag === "function") {
      gtag("event", el.getAttribute("data-track"), {
        destination: el.getAttribute("data-destination") || undefined,
        tool: el.getAttribute("data-tool") || undefined
      });
    }
  });

  // ------------------------------------------------------------- 6. Custom GA4 Key Events Tracking
  document.querySelectorAll("a[href*='apps.microsoft.com']").forEach(function (btn) {
    btn.addEventListener("click", function () {
      if (typeof gtag === "function") {
        gtag("event", "ms_store_click", {
          event_category: "outbound_install",
          event_label: btn.getAttribute("href"),
          tool: btn.getAttribute("data-tool") || "general"
        });
      }
    });
  });

  document.querySelectorAll("a[href*='gumroad.com'], a[href*='buy/']").forEach(function (btn) {
    btn.addEventListener("click", function () {
      if (typeof gtag === "function") {
        gtag("event", "gumroad_checkout_click", {
          event_category: "purchase_intent",
          event_label: btn.getAttribute("href"),
          tool: btn.getAttribute("data-tool") || "general"
        });
      }
    });
  });


  // ------------------------------------------------------------- 7. RFI Tool Download / Launch Feedback Prompt Modal
  function createFeedbackModal() {
    if (document.getElementById("rfiFeedbackModal")) return;

    var modal = document.createElement("div");
    modal.id = "rfiFeedbackModal";
    modal.style.cssText = "position:fixed; inset:0; background:rgba(15,23,42,0.7); backdrop-filter:blur(4px); display:none; align-items:center; justify-content:center; z-index:99999; padding:20px;";
    modal.innerHTML = `
      <div style="background:#ffffff; border:2px solid #000080; border-radius:10px; max-width:500px; width:100%; padding:28px 24px; box-shadow:0 12px 36px rgba(0,0,0,0.25); text-align:center; position:relative; animation:modalPop 0.2s ease-out;">
        <button id="closeRfiModalBtn" style="position:absolute; top:12px; right:14px; background:none; border:none; font-size:22px; cursor:pointer; color:#64748b; line-height:1;">&times;</button>
        <div style="font-size:38px; margin-bottom:8px;">🎉</div>
        <h3 style="font-family:'Space Grotesk',sans-serif; font-size:1.4rem; color:#000080; margin:0 0 10px;">Your Free Tool is Ready!</h3>
        <p style="font-size:0.95rem; color:#334155; line-height:1.6; margin:0 0 20px;">
          This tool is 100% free with no recurring subscriptions or cloud data uploads. 
          <br><br>
          <strong>After trying it on your project</strong>, please take 30 seconds to share your feedback or feature requests directly on our website directory!
        </p>
        <div style="display:flex; flex-direction:column; gap:10px;">
          <a href="feedback.html?tool=rfi" class="btn btn-primary" style="background:#000080; border-color:#000080; padding:12px 20px; justify-content:center; text-align:center; text-decoration:none;">
            ⭐ Give Feedback on Website Directory &rarr;
          </a>
          <button id="dismissRfiModalBtn" class="btn btn-ghost" style="padding:10px 20px; justify-content:center;">
            I'll give feedback later
          </button>
        </div>
      </div>
    `;
    document.body.appendChild(modal);

    document.getElementById("closeRfiModalBtn").addEventListener("click", function() {
      modal.style.display = "none";
    });
    document.getElementById("dismissRfiModalBtn").addEventListener("click", function() {
      modal.style.display = "none";
    });
    modal.addEventListener("click", function(e) {
      if (e.target === modal) modal.style.display = "none";
    });
  }

  createFeedbackModal();

  document.querySelectorAll(".rfi-download-btn, .rfi-launch-btn").forEach(function(el) {
    el.addEventListener("click", function() {
      var modal = document.getElementById("rfiFeedbackModal");
      if (modal) {
        setTimeout(function() {
          modal.style.display = "flex";
        }, 600);
      }
      if (typeof gtag === "function") {
        gtag("event", "rfi_tool_interaction", {
          event_category: "free_tool",
          event_label: el.classList.contains("rfi-download-btn") ? "download" : "launch"
        });
      }
    });
  });




});

// ------------------------------------------------------------- 9. Schedule Heatmap Inspector
window.inspectHeatmap = function(el) {
  if (!el) return;
  var metric = el.getAttribute("data-metric");
  var pkg = el.getAttribute("data-pkg");
  var val = el.getAttribute("data-val");
  var desc = el.getAttribute("data-desc");

  var titleEl = document.getElementById("inspectTitle");
  var textEl = document.getElementById("inspectText");
  var tagEl = document.getElementById("inspectTag");

  if (titleEl) titleEl.innerHTML = "🔍 " + metric + ' &middot; <span style="color:#ffffff">' + pkg + " (" + val + ")</span>";
  if (textEl) textEl.innerHTML = desc;
  if (tagEl) tagEl.innerHTML = "Value: " + val;
};

// ------------------------------------------------------------- 10. Video Walkthrough Timeline Controller
window.jumpTo = function(seconds) {
  var video = document.getElementById("demoVideo");
  if (video) {
    video.currentTime = seconds;
    video.play().catch(function() {});
  }
};

// ------------------------------------------------------------- 11. Interactive Contractor Package Switcher
var pkgData = {
  pkg1: {
    num: "5 parts with sub-area code (e.g. PKG1-SEC1-CIV-0042)",
    sep: "Space / Underscore format",
    col: "Column J (Approval Decision)",
    loc: "Facility & Foundation Areas",
    sla: "94.2%",
    sub: "Average Turnaround: 4.2 Days (FIDIC Target: 7 Days)"
  },
  pkg2: {
    num: "4 parts with zone code (e.g. PKG2-STR-0118)",
    sep: "Mixed format (all three handled)",
    col: "Column J (Engineer Sign-off)",
    loc: "Structural Superstructure Zones",
    sla: "89.6%",
    sub: "Average Turnaround: 5.1 Days (FIDIC Target: 7 Days)"
  },
  pkg3: {
    num: "4 parts with discipline tag (e.g. PKG3-MEP-0089)",
    sep: "Space / Underscore format",
    col: "Column I (Inspection Status)",
    loc: "Underground & Riser Utilities",
    sla: "91.8%",
    sub: "Average Turnaround: 4.8 Days (FIDIC Target: 7 Days)"
  },
  pkg4: {
    num: "4 parts standard (e.g. PKG4-PROC-0205)",
    sep: "Underscore / Hyphen format",
    col: "Column J (Decision Stamped)",
    loc: "Plant Equipment & Handover",
    sla: "96.4%",
    sub: "Average Turnaround: 3.8 Days (FIDIC Target: 7 Days)"
  }
};

window.switchPkg = function(id, btn) {
  document.querySelectorAll(".pkg-tab-btn").forEach(function(b) {
    b.classList.remove("active");
  });
  if (btn) btn.classList.add("active");

  var data = pkgData[id];
  if (!data) return;
  var dNum = document.getElementById("dNum");
  var dSep = document.getElementById("dSep");
  var dCol = document.getElementById("dCol");
  var dLoc = document.getElementById("dLoc");
  var dSla = document.getElementById("dSla");
  var dSlaSub = document.getElementById("dSlaSub");

  if (dNum) dNum.textContent = data.num;
  if (dSep) dSep.textContent = data.sep;
  if (dCol) dCol.textContent = data.col;
  if (dLoc) dLoc.textContent = data.loc;
  if (dSla) dSla.textContent = data.sla;
  if (dSlaSub) dSlaSub.textContent = data.sub;
};

