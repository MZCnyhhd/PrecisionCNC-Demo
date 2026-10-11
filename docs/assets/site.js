/* ==========================================================================
   PrecisionCNC — site interactions
   Plain ES5-safe-ish JS, no dependencies, no network calls.
   Everything here runs locally in the browser so it works on static hosting.
   ========================================================================== */
(function () {
  'use strict';

  function $(sel, root) { return (root || document).querySelector(sel); }
  function $$(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  /* ---------------- Mobile nav ---------------- */
  function initNav() {
    var burger = $('.burger');
    var nav = $('#site-nav');
    if (!burger || !nav) return;
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    $$('#site-nav a').forEach(function (a) {
      a.addEventListener('click', function () {
        nav.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ---------------- Scroll reveal ---------------- */
  function initReveal() {
    var items = $$('.reveal');
    if (!items.length) return;
    if (!('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  }

  /* ---------------- Footer year ---------------- */
  function initYear() {
    $$('[data-year]').forEach(function (el) {
      el.textContent = String(new Date().getFullYear());
    });
  }

  /* ==========================================================================
     Tool 1 — Tolerance vs. cost estimator
     Model: relative unit-cost multiplier by achievable tolerance band,
     with a learning-curve volume factor. Figures are indicative shop rates.
     ========================================================================== */
  var TOL_BANDS = [
    { v: 0.1,   label: '\u00b10.1 mm',   mult: 1.00, name: 'ISO 2768-m general',
      note: 'Standard work. No special process control, first-article check only.',
      inspect: 'Sampling inspection', cmm: 'Not required' },
    { v: 0.05,  label: '\u00b10.05 mm',  mult: 1.45, name: 'Comfortable precision',
      note: 'Well inside normal process capability. Most "precision parts" live here.',
      inspect: 'Dimensional report on all critical features', cmm: 'On critical features' },
    { v: 0.02,  label: '\u00b10.02 mm',  mult: 2.10, name: 'Controlled precision',
      note: 'Tool-wear windows managed, temperature-aware fixturing, often single-setup.',
      inspect: 'Per-batch dimensional report', cmm: 'CMM on first article + sampling' },
    { v: 0.01,  label: '\u00b10.01 mm',  mult: 3.00, name: 'Precision territory',
      note: 'Single-setup machining, temperature-stable inspection. ±10°C shop drift moves a 100 mm steel feature 0.012 mm.',
      inspect: '100% critical-feature inspection', cmm: 'CMM mandatory, every part' },
    { v: 0.005, label: '\u00b10.005 mm or tighter', mult: 4.60, name: 'Capability ceiling',
      note: 'Measurement uncertainty approaches the tolerance itself. Often needs grinding as a secondary process.',
      inspect: '100% inspection, full traceability', cmm: 'CMM mandatory + grinding support' }
  ];

  function volumeFactor(qty) {
    if (qty <= 10) return { f: 1.00, label: 'prototype run' };
    if (qty <= 50) return { f: 0.86, label: 'small batch — fixture amortised' };
    if (qty <= 200) return { f: 0.73, label: 'low-volume production' };
    if (qty <= 1000) return { f: 0.63, label: 'production run — CAM reuse' };
    return { f: 0.57, label: 'volume production' };
  }

  function initToleranceTool() {
    var root = $('#tol-tool');
    if (!root) return;
    var range = $('#tol-range', root);
    var qty = $('#tol-qty', root);
    var out = $('#tol-out', root);
    var bandLabel = $('#tol-band-label', root);
    var costEl = $('#tol-cost', root);
    var chips = $$('.chip', root);
    if (!range || !qty || !out || !bandLabel || !costEl) return;

    function compute() {
      var idx = parseInt(range.value, 10);
      if (isNaN(idx) || idx < 0) idx = 0;
      if (idx > TOL_BANDS.length - 1) idx = TOL_BANDS.length - 1;
      var band = TOL_BANDS[idx];
      var q = parseInt(qty.value, 10);
      if (isNaN(q) || q < 1) q = 1;
      if (q > 100000) q = 100000;

      var vol = volumeFactor(q);
      var mult = band.mult * vol.f;

      bandLabel.textContent = band.label;
      costEl.textContent = mult.toFixed(2) + '\u00d7';

      var html = '';
      html += '<h4>' + band.name + '</h4>';
      html += '<p style="margin:0 0 .6em">' + band.note + '</p>';
      html += '<ul class="ticks" style="margin-top:.4em">';
      html += '<li>Inspection: ' + band.inspect + '</li>';
      html += '<li>CMM: ' + band.cmm + '</li>';
      html += '<li>Quantity ' + q.toLocaleString() + ' \u2014 ' + vol.label +
              ' (\u00d7' + vol.f.toFixed(2) + ' volume factor)</li>';
      html += '</ul>';
      out.className = 'result ready';
      out.innerHTML = html;

      chips.forEach(function (c, i) {
        c.classList.toggle('on', i === idx);
      });
    }

    range.addEventListener('input', compute);
    qty.addEventListener('input', compute);
    chips.forEach(function (c) {
      c.addEventListener('click', function () {
        range.value = (c.getAttribute('data-idx') || '0');
        compute();
      });
    });
    compute();
  }

  /* ==========================================================================
     Tool 2 — Alloy selector (6061 vs 7075)
     ========================================================================== */
  var ALLOY_QS = [
    { id: 'weld',  q: 'Is the part welded or brazed?',            yes: { a: '6061', why: '7075 welds poorly \u2014 cracked joints are a known failure mode.' } },
    { id: 'load',  q: 'Is strength-to-weight the design driver?', yes: { a: '7075', why: '7075-T6 is roughly twice the strength of 6061-T6 (570 vs 310 MPa UTS).' } },
    { id: 'cosm',  q: 'Is it a cosmetic part in black anodize?',  yes: { a: '6061', why: '7075 contains copper: cosmetic Type II anodize goes yellow or mottled. 6061 anodizes clean.' } },
    { id: 'marine',q: 'Does it see salt spray or marine air?',    yes: { a: '6061', why: 'Far lower copper content, meaningfully better corrosion behaviour.' } },
    { id: 'fatig', q: 'Repeated impact or fatigue loading?',      yes: { a: '7075', why: 'Higher fatigue resistance and better dimensional stability under load.' } }
  ];

  function initAlloyTool() {
    var root = $('#alloy-tool');
    if (!root) return;
    var form = $('#alloy-form', root);
    var out = $('#alloy-out', root);

    // build questions
    var html = '';
    ALLOY_QS.forEach(function (item, i) {
      html += '<div class="field" data-q="' + item.id + '">';
      html += '<label>' + (i + 1) + '. ' + item.q + '</label>';
      html += '<div>';
      html += '<button type="button" class="chip on" data-val="no" data-q="' + item.id + '">No / not critical</button> ';
      html += '<button type="button" class="chip" data-val="yes" data-q="' + item.id + '">Yes</button>';
      html += '</div></div>';
    });
    form.innerHTML = html;

    function evaluate() {
      var votes = { '6061': [], '7075': [] };
      ALLOY_QS.forEach(function (item) {
        var on = $('.chip.on[data-q="' + item.id + '"]', form);
        if (on && on.getAttribute('data-val') === 'yes') {
          votes[item.yes.a].push(item.yes.why);
        }
      });

      var n61 = votes['6061'].length, n75 = votes['7075'].length;
      var pick, headline, body = '';

      if (n61 === 0 && n75 === 0) {
        pick = '6061-T6';
        headline = 'The default choice';
        body = '<p>No hard constraints flagged. When a drawing says "aluminium" with no alloy specified, 6061-T6 is what we quote: 20\u201340% cheaper stock, machines slightly faster, welds and anodizes well, and it covers roughly 80% of general CNC work.</p>';
        body += '<p>Revisit the choice if the part later turns out to be structural or impact-loaded.</p>';
      } else if (n75 > n61) {
        pick = '7075-T6';
        headline = 'Strength-driven pick';
        body = '<p>Strength requirements dominate here. 7075-T6 gives roughly twice the ultimate tensile strength of 6061 at similar density, with better fatigue behaviour and less deflection under load.</p>';
        body += '<p><strong>Watch out for:</strong> anodize appearance (copper content shifts colour), machinability (shorter tool life at volume), and no welding.</p>';
      } else if (n61 > n75) {
        pick = '6061-T6';
        headline = 'Practical constraints win';
        body = '<p>Practical constraints outweigh the strength argument. 6061-T6 is the smarter engineering pick unless the load case genuinely demands more.</p>';
      } else {
        pick = 'Price both';
        headline = 'Boundary case \u2014 we quote both alloys';
        body = '<p>You have competing constraints, so the answer is arithmetic rather than opinion: we quote the same part in 6061-T6 and 7075-T6 with the delta stated. On many parts the gap is smaller than customers expect, which turns the decision into a simple calculation.</p>';
      }

      if (votes['6061'].length) {
        body += '<h4 style="margin:1em 0 .3em">Why 6061 scored points</h4><ul class="ticks">';
        votes['6061'].forEach(function (w) { body += '<li>' + w + '</li>'; });
        body += '</ul>';
      }
      if (votes['7075'].length) {
        body += '<h4 style="margin:1em 0 .3em">Why 7075 scored points</h4><ul class="ticks">';
        votes['7075'].forEach(function (w) { body += '<li>' + w + '</li>'; });
        body += '</ul>';
      }

      out.className = 'result ready';
      out.innerHTML = '<div class="big" style="font-size:1.5rem">' + pick + '</div>' +
                      '<h4 style="margin-top:.5em">' + headline + '</h4>' + body;
    }

    form.addEventListener('click', function (e) {
      var btn = e.target.closest ? e.target.closest('.chip') : null;
      if (!btn || !form.contains(btn)) return;
      var q = btn.getAttribute('data-q');
      $$('.chip[data-q="' + q + '"]', form).forEach(function (b) { b.classList.remove('on'); });
      btn.classList.add('on');
      evaluate();
    });

    evaluate();
  }

  /* ==========================================================================
     RFQ form — client-side only. No backend on this static build.
     ========================================================================== */
  function initRfq() {
    var form = $('#rfq-form');
    if (!form) return;
    var drop = $('#rfq-drop', form);
    var input = $('#rfq-files', form);
    var list = $('#rfq-filelist', form);
    var status = $('#rfq-status', form);
    var files = [];

    function render() {
      list.innerHTML = '';
      files.forEach(function (f, i) {
        var li = document.createElement('li');
        var left = document.createElement('span');
        left.textContent = f.name + ' \u2014 ' + (f.size / 1048576).toFixed(2) + ' MB';
        var rm = document.createElement('button');
        rm.type = 'button';
        rm.className = 'rm';
        rm.setAttribute('aria-label', 'Remove ' + f.name);
        rm.textContent = '\u2715';
        rm.addEventListener('click', function () { files.splice(i, 1); render(); });
        li.appendChild(left);
        li.appendChild(rm);
        list.appendChild(li);
      });
    }

    function addFiles(fileList) {
      Array.prototype.forEach.call(fileList, function (f) {
        if (files.length >= 5) return;
        files.push(f);
      });
      render();
    }

    if (drop && input) {
      drop.addEventListener('click', function () { input.click(); });
      input.addEventListener('change', function () { addFiles(input.files); input.value = ''; });
      ['dragenter', 'dragover'].forEach(function (ev) {
        drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add('hot'); });
      });
      ['dragleave', 'drop'].forEach(function (ev) {
        drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove('hot'); });
      });
      drop.addEventListener('drop', function (e) {
        if (e.dataTransfer && e.dataTransfer.files) addFiles(e.dataTransfer.files);
      });
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var required = $$('[required]', form);
      var missing = required.filter(function (el) { return !String(el.value || '').trim(); });
      if (missing.length) {
        status.className = 'form-note';
        status.style.color = '#C2410C';
        status.textContent = 'Please complete the required fields marked with *.';
        missing[0].focus();
        return;
      }
      var name = ($('#rfq-name', form) || {}).value || '';
      status.className = 'result ready';
      status.style.color = '';
      status.innerHTML =
        '<h4>Validation passed \u2014 ' + (name ? 'thanks, ' + name.split(' ')[0] + '. ' : '') + '</h4>' +
        '<p>This is a <strong>static demonstration build</strong>, so nothing was transmitted anywhere: there is no server to receive it. On the production WordPress build this form is Fluent Forms with file upload enabled, wired to WP Mail SMTP, and the submission lands in the shop inbox with the STEP file attached.</p>' +
        '<p class="small" style="margin-bottom:0">Files staged in this session: ' + files.length + ' &middot; Required fields validated: ' + required.length + '</p>';
      status.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
  }

  /* ---------------- Boot ---------------- */
  function boot() {
    initNav();
    initReveal();
    initYear();
    initToleranceTool();
    initAlloyTool();
    initRfq();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
