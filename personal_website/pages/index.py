"""Home page — assembles all sections."""

import reflex as rx

from ..components import (
    hero_section,
    nav_section,
    about_section,
    work_section,
    cta_section,
    til_section,
    contact_section,
    footer_section,
)


# JavaScript for intro overlay removal, scroll reveal, floating name, and tittle flash
_SITE_SCRIPTS = """
// Wait for all required DOM elements before initializing.
// Reflex SPA hydration may delay element availability.
(function() {
  var attempts = 0;
  var maxAttempts = 50; // 50 * 100ms = 5s max wait

  function waitForElements() {
    attempts++;
    var floating = document.querySelector('.floating-name');
    var heroName = document.querySelector('.hero-name');
    var hero = document.querySelector('.hero');
    var pageNav = document.querySelector('.page-nav');
    var intro = document.querySelector('.intro');

    if ((!floating || !heroName || !hero || !pageNav) && attempts < maxAttempts) {
      setTimeout(waitForElements, 100);
      return;
    }

    // All elements found (or gave up) — initialize everything
    initAll(floating, heroName, hero, pageNav, intro);
  }

  function initAll(floating, heroName, hero, pageNav, intro) {
    // ── Remove intro overlay after animation ──
    if (intro) {
      intro.addEventListener('animationend', function() {
        intro.remove();
      });
    }

    // ── Scroll reveal (IntersectionObserver) ──
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal').forEach(function(el) {
      observer.observe(el);
    });

    // ── Floating name scroll transition ──
    if (floating && heroName && hero && pageNav) {
      var line1 = floating.querySelector('.fn-line1');
      var line2 = floating.querySelector('.fn-line2');

      if (line1 && line2) {
        var heroStartX, heroStartY, heroFS, navEndX, navEndY;
        var navLine1W, heroH;
        var ticking = false, active = false;

        function measure() {
          var scroll = window.scrollY;
          var hRect = heroName.getBoundingClientRect();
          heroStartX = hRect.left;
          heroStartY = hRect.top + scroll;
          heroFS = parseFloat(getComputedStyle(heroName).fontSize);
          heroH = hero.offsetHeight;

          var navNameEl = pageNav.querySelector('.nav-name');
          if (!navNameEl) return;
          var navNameRect = navNameEl.getBoundingClientRect();
          var navRect = pageNav.getBoundingClientRect();
          navEndX = navNameRect.left;
          navEndY = navNameRect.top - navRect.top;

          line1.style.display = 'inline';
          floating.style.fontSize = '18px';
          navLine1W = line1.getBoundingClientRect().width;
          floating.style.fontSize = heroFS + 'px';
          line1.style.display = '';
        }

        function init() {
          measure();
          document.body.classList.add('fn-active');
          active = true;
          update();
        }

        function lerp(a, b, t) { return a + (b - a) * t; }

        function update() {
          if (!active) return;
          var scrollY = window.scrollY;
          var raw = Math.min(Math.max(scrollY / heroH, 0), 1);
          var t = raw * raw * (3 - 2 * raw);

          var naturalY = heroStartY - scrollY;
          var x = lerp(heroStartX, navEndX, t);
          var y = Math.max(lerp(naturalY, navEndY, t), navEndY);
          var fs = lerp(heroFS, 18, t);
          var lh = lerp(0.88, 1.2, t);

          floating.style.transform = 'translate(' + x + 'px,' + y + 'px)';
          floating.style.fontSize = fs + 'px';
          floating.style.lineHeight = lh;
          floating.style.fontWeight = 400;
          floating.style.color = '#fff';

          var line1W = navLine1W * (fs / 18);
          var spaceW = fs * 0.22;
          var currentLH = fs * lh;
          line2.style.transform = 'translate(' + (t * (line1W + spaceW)) + 'px,' + (-t * currentLH) + 'px)';
        }

        window.addEventListener('scroll', function() {
          if (!ticking) {
            requestAnimationFrame(function() {
              update();
              ticking = false;
            });
            ticking = true;
          }
        });

        var resizeTimer;
        window.addEventListener('resize', function() {
          clearTimeout(resizeTimer);
          resizeTimer = setTimeout(function() {
            measure();
            update();
          }, 150);
        });

        // Wait for intro animation to finish before starting float
        setTimeout(init, 2100);
      }
    }

    // ── Tittle flash effect on the "i" dots ──
    var tittles = document.querySelectorAll('.tittle-i');
    if (tittles.length > 0) {
      function flash() {
        tittles.forEach(function(el, i) {
          setTimeout(function() {
            el.classList.remove('flash');
            void el.offsetWidth;
            el.classList.add('flash');
            el.addEventListener('animationend', function handler() {
              el.classList.remove('flash');
              el.removeEventListener('animationend', handler);
            });
          }, i * 150);
        });
      }
      setTimeout(flash, 3000);
      setInterval(flash, 15000);
    }
  }

  // Start polling for elements
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', waitForElements);
  } else {
    waitForElements();
  }
})();
"""


def index_page() -> rx.Component:
    """Complete home page with all sections and injected JavaScript."""
    return rx.fragment(
        hero_section(),
        # Page wrapper
        rx.el.div(
            nav_section(),
            about_section(),
            rx.el.hr(),
            work_section(),
            rx.el.hr(),
            cta_section(),
            til_section(),
            rx.el.hr(),
            contact_section(),
            footer_section(),
            class_name="page",
        ),
        # Fixed CTA button
        rx.el.a(
            "Let's talk ↗",
            href="#contact",
            class_name="fixed-cta",
        ),
        # Inject all JavaScript
        rx.script(_SITE_SCRIPTS),
    )
