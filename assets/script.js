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
    var end = new Date(timerEl.getAttribute("data-deadline") || "2026-09-30T23:59:59+03:00");
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
});
