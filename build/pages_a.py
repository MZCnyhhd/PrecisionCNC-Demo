# -*- coding: utf-8 -*-
"""Body HTML for Home, Capabilities and Materials.

Internal links are written as ``@/some/path/`` and rewritten to page-relative
URLs by the generator, so the same body markup works at any folder depth.
"""

HOME = r"""
<section class="hero">
  <div class="wrap">
    <div class="hero-in">
      <span class="eyebrow">ISO 9001:2015 &middot; Dongguan, China &middot; 45 machining centres</span>
      <h1>Precision CNC Machining Services &mdash; 5&#8209;Axis &amp; Custom Parts</h1>
      <p class="lede">We machine custom metal and plastic parts from prototype to production:
      5-axis CNC milling, CNC turning and combined mill-turn work in aluminium, stainless steel,
      titanium and engineering plastics. Tolerances to &plusmn;0.005&nbsp;mm, prototypes in
      5&ndash;7 days.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="@/contact/">Upload Files &amp; Get a Quote</a>
        <a class="btn btn-ghost" href="@/capabilities/">See Our Capabilities</a>
      </div>
    </div>
  </div>
  <div class="wrap">
    <div class="hero-stats">
      <div><b>45</b><span>CNC machining centres</span></div>
      <div><b>8</b><span>Five-axis machines</span></div>
      <div><b>&plusmn;0.005&nbsp;mm</b><span>Tolerance capability</span></div>
      <div><b>24&nbsp;h</b><span>Engineered quote turnaround</span></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="sec-kicker">What we machine</span>
      <h2>Four processes, one shop floor</h2>
      <p>Nothing critical is subcontracted. The fixture that makes your three prototypes makes
      your three hundred production parts &mdash; which is why delivery dates hold.</p>
    </div>
    <div class="grid g4">
      <article class="card reveal">
        <h3><span class="ico"><svg viewBox="0 0 24 24"><path d="M12 2v6"/><path d="M12 8l5 9H7l5-9z"/><circle cx="12" cy="20" r="2"/></svg></span>5-Axis Milling</h3>
        <p>Complex geometries, undercuts and single-setup accuracy for aerospace, medical and
        UAV parts. Impellers, turbine components, organic brackets.</p>
        <p class="small" style="margin:0"><a href="@/capabilities/#five-axis">Machines &amp; envelope &rarr;</a></p>
      </article>
      <article class="card reveal">
        <h3><span class="ico"><svg viewBox="0 0 24 24"><rect x="3" y="9" width="18" height="6" rx="3"/><path d="M3 12H1M23 12h-2M7 9V6M17 15v3"/></svg></span>CNC Turning &amp; Mill-Turn</h3>
        <p>Shafts, bushings and rotational parts up to &Oslash;300&nbsp;mm with live tooling,
        C-axis milling and in-process probing.</p>
        <p class="small" style="margin:0"><a href="@/capabilities/#turning">Turning capability &rarr;</a></p>
      </article>
      <article class="card reveal">
        <h3><span class="ico"><svg viewBox="0 0 24 24"><path d="M4 19h16"/><path d="M6 19V8l6-4 6 4v11"/><path d="M10 19v-5h4v5"/></svg></span>Prototype Machining</h3>
        <p>1&ndash;10 piece runs in 5&ndash;7 working days for product development, form-fit
        testing and design validation.</p>
        <p class="small" style="margin:0"><a href="@/contact/">Start with one part &rarr;</a></p>
      </article>
      <article class="card reveal">
        <h3><span class="ico"><svg viewBox="0 0 24 24"><path d="M3 6h18M3 12h18M3 18h18"/><circle cx="8" cy="6" r="2"/><circle cx="16" cy="12" r="2"/><circle cx="11" cy="18" r="2"/></svg></span>Low-Volume Production</h3>
        <p>10&ndash;5,000 pieces with documented process control, SPC charts and repeatable
        anodise colour batches.</p>
        <p class="small" style="margin:0"><a href="@/capabilities/">Production process &rarr;</a></p>
      </article>
    </div>
  </div>
</section>

<section class="sec-alt">
  <div class="wrap">
    <div class="grid g2" style="align-items:center;gap:52px">
      <div class="reveal">
        <span class="sec-kicker">Capability snapshot</span>
        <h2>What the shop floor actually holds</h2>
        <p>45 CNC machining centres across a 4,000&nbsp;m&sup2; facility, 22 of our 80 staff in
        engineering and quality. That ratio &mdash; not the machine count &mdash; decides whether
        a machine shop solves problems or just runs parts.</p>
        <dl style="margin:1.6rem 0 0">
          <div class="spec"><dt>Machines</dt><dd>45 CNC machining centres, including 8 five-axis</dd></div>
          <div class="spec"><dt>Tolerance</dt><dd>&plusmn;0.005&nbsp;mm on critical dimensions; &plusmn;0.002&nbsp;mm with grinding support</dd></div>
          <div class="spec"><dt>Smallest feature</dt><dd>&Oslash;0.3&nbsp;mm holes; features down to 0.3&nbsp;mm</dd></div>
          <div class="spec"><dt>Turning envelope</dt><dd>&Oslash;1&nbsp;mm to &Oslash;300&nbsp;mm, live tooling and C-axis</dd></div>
          <div class="spec"><dt>Inspection</dt><dd>Zeiss CMM, optical comparator, surface roughness tester</dd></div>
          <div class="spec"><dt>Certification</dt><dd>ISO 9001:2015; EN 10204 3.1 material certificates</dd></div>
        </dl>
      </div>
      <div class="reveal">
        <div class="tool">
          <div class="tool-head"><span class="dot"></span><h3>Lead time by order type</h3></div>
          <div class="tool-body">
            <div class="spec"><dt>1&ndash;10 pieces</dt><dd>5&ndash;7 working days</dd></div>
            <div class="spec"><dt>11&ndash;50 pieces</dt><dd>7&ndash;10 working days</dd></div>
            <div class="spec"><dt>51&ndash;200 pieces</dt><dd>10&ndash;15 working days</dd></div>
            <div class="spec"><dt>201&ndash;1,000 pieces</dt><dd>15&ndash;22 working days</dd></div>
            <div class="spec"><dt>1,000+ pieces</dt><dd>Scheduled per release, quoted with a delivery plan</dd></div>
            <div class="spec" style="border-top:1px solid var(--line);margin-top:6px;padding-top:16px">
              <dt>Expedite</dt><dd>Ask. Genuine rush slots exist when the shop has capacity &mdash; we will tell you honestly rather than promise and ship late.</dd></div>
          </div>
        </div>
        <p class="small" style="margin-top:14px">Lead times run from drawing release and material
        availability. Titanium and 17-4PH stock lead time is quoted per order.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="sec-kicker">Free engineering tool</span>
      <h2>What does your tolerance actually cost?</h2>
      <p>Tolerance callouts are where design intent and machining cost collide. Move the slider to
      see how tighter bands change the process &mdash; and why they do.</p>
    </div>
    <div class="grid g2" style="gap:44px;align-items:start">
      <div class="tool reveal" id="tol-tool" style="grid-column:1/-1;max-width:900px;margin:0 auto">
        <div class="tool-head"><span class="dot"></span><h3>Tolerance &rarr; cost estimator</h3></div>
        <div class="tool-body">
          <ul class="chips">
            <li><button type="button" class="chip on" data-idx="0">&plusmn;0.1 mm</button></li>
            <li><button type="button" class="chip" data-idx="1">&plusmn;0.05 mm</button></li>
            <li><button type="button" class="chip" data-idx="2">&plusmn;0.02 mm</button></li>
            <li><button type="button" class="chip" data-idx="3">&plusmn;0.01 mm</button></li>
            <li><button type="button" class="chip" data-idx="4">&plusmn;0.005 mm</button></li>
          </ul>
          <div class="range-out">
            <label for="tol-range" style="font-weight:700;font-size:.87rem;color:var(--navy)">Achievable tolerance</label>
            <b id="tol-band-label">&plusmn;0.1 mm</b>
          </div>
          <input type="range" id="tol-range" min="0" max="4" step="1" value="0"
                 aria-label="Tolerance band">
          <div class="row2" style="margin-top:16px">
            <div class="field" style="margin-bottom:0">
              <label for="tol-qty">Order quantity <span class="hint">&mdash; drives the volume factor</span></label>
              <input type="number" id="tol-qty" value="10" min="1" max="100000" step="1">
            </div>
            <div class="range-out" style="align-items:center;margin-bottom:0">
              <span style="font-weight:700;font-size:.87rem;color:var(--navy)">Relative unit cost</span>
              <b id="tol-cost" style="font-size:1.7rem">1.00&times;</b>
            </div>
          </div>
          <div class="result ready" id="tol-out" style="margin-top:20px"></div>
          <p class="form-note">Indicative model, not a quotation. Relative to an unmarked drawing
          quoted at ISO&nbsp;2768-m. Your actual price depends on geometry, material and feature
          count &mdash; send the drawing and we will price it properly.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="sec-kicker">Industries</span>
      <h2>Who we machine for</h2>
      <p>Product development teams and hardware companies across Europe, North America and Asia
      &mdash; usually the awkward middle ground between local prototype shops and mass
      production.</p>
    </div>
    <div class="grid g3">
      <a class="card reveal" href="@/industries/#medical" style="display:block">
        <h3>Medical Devices</h3>
        <p>316L and PEEK prototypes, surgical instruments and device enclosures with
        design-control documentation.</p>
      </a>
      <a class="card reveal" href="@/industries/#aerospace" style="display:block">
        <h3>Aerospace &amp; UAV</h3>
        <p>5-axis structural brackets and airframe parts in 7075 and titanium, with
        AS9102-style FAI reporting.</p>
      </a>
      <a class="card reveal" href="@/industries/#robotics" style="display:block">
        <h3>Robotics &amp; Automation</h3>
        <p>Actuator housings, harmonic drive components and custom end-of-arm tooling that
        repeats batch to batch.</p>
      </a>
      <a class="card reveal" href="@/industries/#automotive" style="display:block">
        <h3>Automotive &amp; EV</h3>
        <p>Test rigs, prototype components and charging infrastructure parts with
        PPAP-style dimensional reporting.</p>
      </a>
      <a class="card reveal" href="@/industries/#semiconductor" style="display:block">
        <h3>Semiconductor Fixtures</h3>
        <p>Vacuum-compatible aluminium and stainless fixtures, PEEK insulators and
        clean-finish requirements.</p>
      </a>
      <a class="card reveal" href="@/industries/#electronics" style="display:block">
        <h3>Consumer Electronics</h3>
        <p>Bead-blast and anodised appearance parts with colour consistency managed
        per batch.</p>
      </a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="grid g2" style="gap:52px;align-items:start">
      <div class="reveal">
        <span class="sec-kicker">How quoting works</span>
        <h2>From file upload to quotation in 24 hours</h2>
        <ol class="steps" style="margin-top:1.6rem">
          <li><b>You send STEP + drawing</b>Upload your 3D file (STEP or IGES) and a 2D PDF
          marking critical tolerances, finishes and threads. Not sure what to send?
          <a href="@/blog/how-to-prepare-cad-files-rfq/">Read the RFQ guide &rarr;</a></li>
          <li><b>An engineer reviews it</b>Not a sales script. Material and tolerance advice is
          included in the reply, including where we think your drawing is over-specified.</li>
          <li><b>You get priced options</b>Unit pricing at your quantity, price breaks at higher
          volumes, finish options, and an honest delivery date.</li>
          <li><b>First article proves it</b>Every new part number ships with a CMM first-article
          report. You see the numbers before you commit to volume.</li>
        </ol>
        <a class="btn btn-primary mt1" href="@/contact/">Upload Files &amp; Get a Quote</a>
      </div>
      <div class="reveal">
        <span class="sec-kicker">Common questions</span>
        <h2>Before you ask</h2>
        <div style="margin-top:1.6rem">
          <div class="card" style="margin-bottom:14px">
            <h3>What is your minimum order quantity?</h3>
            <p style="margin:0">One piece. Prototypes from a single part are how most of our
            customer relationships start &mdash; it is the cheapest place to test a machine shop.</p>
          </div>
          <div class="card" style="margin-bottom:14px">
            <h3>How fast can I get a quote?</h3>
            <p style="margin:0">Within 24 hours of receiving a STEP file and a 2D drawing. The
            reply includes unit pricing, price breaks, material and finish recommendations, and
            a delivery date we intend to keep.</p>
          </div>
          <div class="card" style="margin-bottom:14px">
            <h3>Drawings only, or do you need 3D CAD?</h3>
            <p style="margin:0">We need 3D geometry to quote accurately. STEP or IGES is ideal
            &mdash; export STEP from whatever CAD package you use rather than sending native files.</p>
          </div>
          <div class="card">
            <h3>Do you sign NDAs?</h3>
            <p style="margin:0">Yes. Send yours and we return a signed copy before you release
            files, or ask us for a mutual NDA template.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec-alt">
  <div class="wrap">
    <div class="cta-band reveal">
      <div>
        <h2>Start with one part</h2>
        <p>Test us where it is cheapest to test &mdash; a prototype. Upload a STEP file and a
        marked-up drawing; you will have engineering feedback and a price within 24 hours.</p>
      </div>
      <a class="btn btn-primary" href="@/contact/">Upload Files &amp; Get a Quote</a>
    </div>
  </div>
</section>
"""


CAPABILITIES = r"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Capabilities</span>
    <h1>CNC Machining Capabilities</h1>
    <p>Everything below is done in-house in our 4,000&nbsp;m&sup2; Dongguan facility &mdash;
    nothing critical is subcontracted, which is why our delivery dates hold.</p>
  </div>
</section>

<section id="five-axis">
  <div class="wrap">
    <div class="grid g2" style="gap:52px;align-items:start">
      <div class="reveal">
        <span class="sec-kicker">01 &mdash; Milling</span>
        <h2>5-Axis CNC Milling</h2>
        <p>Eight five-axis machining centres for geometries that would need five setups on
        3-axis machines &mdash; or cannot be made on them at all. Impellers, turbine components,
        complex housings, orthopaedic trial parts.</p>
        <p>Single-setup machining removes cumulative tolerance stack-up: position accuracy between
        features stays within <strong>&plusmn;0.01&nbsp;mm</strong> regardless of part complexity.
        Tilting the part instead of extending the tool also lets short, rigid cutters reach deep
        pockets &mdash; better finish, no chatter, faster feeds.</p>
        <div class="callout">
          <p><strong>Not every part needs five axes.</strong> A 100-piece order of flat brackets
          on a 3-axis machine can cost 40% less than the same parts on a 5-axis machine, at
          identical quality. We route jobs by what the part needs, not by which machine looks
          impressive in a quotation.</p>
        </div>
        <p class="small">Want the full decision logic? <a href="@/blog/5-axis-cnc-machining-when-needed/">When your
        project actually needs 5-axis machining &rarr;</a></p>
      </div>
      <div class="reveal">
        <div class="tool">
          <div class="tool-head"><span class="dot"></span><h3>5-axis envelope</h3></div>
          <div class="tool-body">
            <div class="spec"><dt>Machines</dt><dd>8 five-axis machining centres</dd></div>
            <div class="spec"><dt>Travel</dt><dd>Up to 800 &times; 600 &times; 500&nbsp;mm</dd></div>
            <div class="spec"><dt>Spindle</dt><dd>12,000&ndash;20,000&nbsp;rpm, HSK-A63</dd></div>
            <div class="spec"><dt>Position accuracy</dt><dd>&plusmn;0.01&nbsp;mm between features, single setup</dd></div>
            <div class="spec"><dt>Typical parts</dt><dd>Impellers &middot; turbine components &middot; organic brackets &middot; housings with undercuts</dd></div>
            <div class="spec"><dt>CAM</dt><dd>HyperMILL / NX, full simulation before cutting</dd></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec-alt" id="turning">
  <div class="wrap">
    <div class="grid g2" style="gap:52px;align-items:start">
      <div class="reveal">
        <div class="tool">
          <div class="tool-head"><span class="dot"></span><h3>Turning envelope</h3></div>
          <div class="tool-body">
            <div class="spec"><dt>Machines</dt><dd>40+ lathes including live-tooling mill-turn centres</dd></div>
            <div class="spec"><dt>Diameter</dt><dd>&Oslash;1&nbsp;mm to &Oslash;300&nbsp;mm</dd></div>
            <div class="spec"><dt>Capability</dt><dd>Thread whirling, C-axis milling, in-process probing, bar feed to &Oslash;80&nbsp;mm</dd></div>
            <div class="spec"><dt>Typical parts</dt><dd>Shafts &middot; bushings &middot; fittings &middot; connectors &middot; cross-drilled turned parts</dd></div>
            <div class="spec"><dt>Surface finish</dt><dd>Ra 0.4&nbsp;&micro;m achievable on turned diameters</dd></div>
            <div class="spec"><dt>Threads</dt><dd>Metric, UNC/UNF, NPT, BSPP, trapezoidal to drawing</dd></div>
          </div>
        </div>
      </div>
      <div class="reveal">
        <span class="sec-kicker">02 &mdash; Turning</span>
        <h2>CNC Turning &amp; Mill-Turn</h2>
        <p>Forty-plus lathes including live-tooling mill-turn centres, covering a
        &Oslash;1&nbsp;mm to &Oslash;300&nbsp;mm envelope.</p>
        <p>The interesting parts are the ones that are round and then not-quite-round:
        cross-holes, flats, milled slots and axial ports on turned blanks. Doing those in one
        setup on a mill-turn centre removes the second fixture &mdash; and with it, the
        concentricity error that comes from re-chucking.</p>
        <ul class="ticks">
          <li>In-process probing verifies critical diameters without unclamping</li>
          <li>Bar feed to &Oslash;80&nbsp;mm for unattended production runs</li>
          <li>Thread whirling for long, thin, high-precision threads</li>
          <li>Sub-spindle pick-off completes the back of the part in cycle</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section id="tolerances">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="sec-kicker">03 &mdash; Precision</span>
      <h2>Tolerances &amp; Precision</h2>
      <p>Standard tolerance ISO 2768-m; capability to &plusmn;0.005&nbsp;mm on critical
      dimensions, &plusmn;0.002&nbsp;mm with grinding support. CMM verification on first
      articles; SPC charts for production runs above 500 pieces.</p>
    </div>
    <div class="grid g2" style="gap:44px;align-items:start">
      <div class="reveal">
        <div class="tbl-wrap">
          <table>
            <thead>
              <tr><th>Band</th><th>What it means in practice</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>&plusmn;0.1&nbsp;mm</strong><br><span class="small">ISO 2768-m</span></td>
                  <td>The default for any competent shop. Correct for housings, brackets and
                  non-mating features on an unmarked drawing.</td></tr>
              <tr><td><strong>&plusmn;0.05&nbsp;mm</strong></td>
                  <td>Comfortable precision work with good process control. Most &ldquo;precision
                  parts&rdquo; live here without drama.</td></tr>
              <tr><td><strong>&plusmn;0.01&nbsp;mm</strong></td>
                  <td>Precision territory. Requires controlled processes, temperature-stable
                  inspection, and often single-setup machining. Bearing bores and precision
                  locating features.</td></tr>
              <tr><td><strong>&plusmn;0.005&nbsp;mm</strong></td>
                  <td>Capability ceiling. CMM verification mandatory, sometimes grinding as a
                  secondary process. Gauge elements, high-pressure sealing fits, optical
                  mounts.</td></tr>
            </tbody>
          </table>
        </div>
        <p class="small" style="margin-top:14px">Full explanation, including why tighter
        tolerances cost disproportionately more:
        <a href="@/blog/cnc-machining-tolerances-explained/">Understanding CNC machining tolerances &rarr;</a></p>
      </div>
      <div class="reveal">
        <div class="tool" id="tol-tool">
          <div class="tool-head"><span class="dot"></span><h3>Tolerance &rarr; cost estimator</h3></div>
          <div class="tool-body">
            <div class="range-out">
              <label for="tol-range" style="font-weight:700;font-size:.87rem;color:var(--navy)">Achievable tolerance</label>
              <b id="tol-band-label">&plusmn;0.1 mm</b>
            </div>
            <input type="range" id="tol-range" min="0" max="4" step="1" value="0"
                   aria-label="Tolerance band">
            <div class="row2" style="margin-top:16px">
              <div class="field" style="margin-bottom:0">
                <label for="tol-qty">Order quantity</label>
                <input type="number" id="tol-qty" value="10" min="1" max="100000" step="1">
              </div>
              <div class="range-out" style="align-items:center;margin-bottom:0">
                <span style="font-weight:700;font-size:.87rem;color:var(--navy)">Relative cost</span>
                <b id="tol-cost" style="font-size:1.7rem">1.00&times;</b>
              </div>
            </div>
            <div class="result ready" id="tol-out" style="margin-top:18px"></div>
          </div>
        </div>
        <div class="callout callout-navy" style="margin-top:20px">
          <p><strong>Mark what matters.</strong> Quoting every feature at &plusmn;0.005&nbsp;mm
          prices the whole part like a gauge block. Mark the functional dimensions on the drawing
          and let the rest ride at standard tolerance &mdash; that habit typically saves
          15&ndash;25% on precision parts.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec-alt" id="finishing">
  <div class="wrap">
    <div class="grid g2" style="gap:52px;align-items:start">
      <div class="reveal">
        <span class="sec-kicker">04 &mdash; Finishing</span>
        <h2>Finishing &amp; Surface Treatment</h2>
        <p>Finishing is coordinated and inspected by us, with samples approved before the batch
        runs. Colour consistency is managed per order &mdash; anodise batches are tracked so
        batch 200 matches batch 2.</p>
        <ul class="ticks">
          <li><strong>Anodising</strong> &mdash; Type II decorative and Type III hard anodise, chromic and
          sulphuric, with colour matching across a batch</li>
          <li><strong>Passivation</strong> &mdash; per ASTM A967, standard on stainless medical and
          marine parts</li>
          <li><strong>Black oxide</strong> &mdash; tooling, fixtures and wear surfaces</li>
          <li><strong>Electroplating</strong> &mdash; zinc, nickel, electroless nickel</li>
          <li><strong>Bead blasting</strong> &mdash; uniform matte prep before anodise, and a finished
          texture in its own right</li>
          <li><strong>Laser engraving</strong> &mdash; part marking, serialisation and UID compliance</li>
        </ul>
      </div>
      <div class="reveal">
        <span class="sec-kicker">05 &mdash; Inspection</span>
        <h2>Inspection &amp; Assembly</h2>
        <p>Zeiss CMM, height gauges, thread gauges, optical comparator and surface roughness
        tester. A dimensional report ships with every order; a full FAI package
        (AS9102-style) is available on request.</p>
        <div class="spec" style="padding-top:0"><dt>First article</dt><dd>CMM verified on every new
        part number before the run is released</dd></div>
        <div class="spec"><dt>In-process</dt><dd>Probing on mill-turn work; SPC and Cpk reporting on
        runs above 500 pieces</dd></div>
        <div class="spec"><dt>Final</dt><dd>100% inspection on critical features, AQL sampling on
        general dimensions</dd></div>
        <div class="spec" style="border-bottom:0"><dt>Assembly</dt><dd>Light mechanical assembly,
        pressing, helicoil and thread-insert installation</dd></div>
        <p style="margin-top:1.6rem"><a class="btn btn-outline" href="@/quality/">Quality control in detail</a></p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="sec-kicker">Equipment list</span>
      <h2>Machine park</h2>
      <p>45 machining centres, all under one roof. Nothing critical is subcontracted.</p>
    </div>
    <div class="tbl-wrap reveal">
      <table>
        <thead>
          <tr><th>Category</th><th>Qty</th><th>Type &amp; envelope</th><th>Best suited to</th></tr>
        </thead>
        <tbody>
          <tr><td>5-axis machining centres</td><td>8</td><td>Trunnion &amp; gantry, to 800&times;600&times;500&nbsp;mm</td>
              <td>Complex geometry, tight inter-feature position, deep pockets</td></tr>
          <tr><td>3-axis vertical machining centres</td><td>22</td><td>To 1,200&times;600&times;600&nbsp;mm</td>
              <td>Plates, brackets, housings, high-volume simple geometry</td></tr>
          <tr><td>CNC lathes with live tooling</td><td>9</td><td>&Oslash;1&ndash;300&nbsp;mm, bar feed to &Oslash;80&nbsp;mm</td>
              <td>Shafts, bushings, fittings, cross-drilled rotational parts</td></tr>
          <tr><td>Mill-turn centres</td><td>4</td><td>Sub-spindle, C-axis, in-process probing</td>
              <td>Round-then-not-round parts completed in one setup</td></tr>
          <tr><td>Surface &amp; cylindrical grinders</td><td>2</td><td>To &plusmn;0.002&nbsp;mm</td>
              <td>Secondary operations on capability-ceiling tolerances</td></tr>
        </tbody>
      </table>
    </div>
    <div class="grid g2" style="gap:44px;margin-top:44px;align-items:start">
      <div class="reveal">
        <h2>Materials we machine daily</h2>
        <p>Aluminium 6061-T6 and 7075-T6 &middot; Stainless 303, 304, 316L and 17-4PH &middot;
        Titanium Grade 2 and Grade 5 &middot; Brass C360 &middot; Copper &middot; Engineering
        plastics including PEEK, Delrin, Nylon and PTFE.</p>
        <p>Material certificates (EN 10204 3.1) ship with metal orders, and we can supply positive
        material identification on request.</p>
        <a class="btn btn-outline" href="@/materials/">Materials &amp; selection guidance</a>
      </div>
      <div class="reveal">
        <div class="callout">
          <p><strong>Have an unusual requirement?</strong> Hardened tool steel, Inconel,
          beryllium copper, ceramics or a material we have not listed &mdash; send the
          specification and an engineer will tell you honestly whether it is work we should take.
          We would rather decline than learn on your part.</p>
        </div>
        <a class="btn btn-primary" href="@/contact/">Send your drawing</a>
      </div>
    </div>
  </div>
</section>
"""


MATERIALS = r"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Materials</span>
    <h1>Materials We Machine</h1>
    <p>Material choice drives cost, weight, corrosion behaviour and machining time. This page is
    what our engineers actually recommend &mdash; not a metal catalogue. When a cheaper alloy does
    the job, we say so in the quote.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="sec-kicker">Interactive</span>
      <h2>Which alloy do you actually need?</h2>
      <p>Answer five questions and we will tell you which side of the 6061 / 7075 line your part
      falls on &mdash; the same logic our quoting desk uses.</p>
    </div>
    <div class="tool reveal" id="alloy-tool" style="max-width:900px;margin:0 auto">
      <div class="tool-head"><span class="dot"></span><h3>Aluminium alloy selector &mdash; 6061 vs 7075</h3></div>
      <div class="tool-body">
        <div id="alloy-form"></div>
        <div class="result" id="alloy-out"></div>
        <p class="form-note">Decision aid only. Send the application &mdash; loads, environment,
        finish &mdash; and the quotation states the alloy with its reasoning.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="sec-kicker">Aluminium</span>
      <h2>Aluminium alloys</h2>
      <p>Roughly 60% of what we machine is aluminium. Three alloys cover almost every job.</p>
    </div>
    <div class="grid g3">
      <article class="card reveal">
        <h3>6061-T6</h3>
        <p class="small" style="margin-bottom:.8em">310&nbsp;MPa UTS &middot; the default</p>
        <p>Good strength, excellent machinability, weldable, anodises beautifully. Around 80% of
        our aluminium work.</p>
        <ul class="ticks" style="margin-bottom:0">
          <li>Enclosures, brackets, fixtures, heat sinks</li>
          <li>Cosmetic black anodise parts</li>
          <li>Welded assemblies</li>
          <li>Marine-adjacent environments</li>
        </ul>
      </article>
      <article class="card reveal">
        <h3>7075-T6</h3>
        <p class="small" style="margin-bottom:.8em">570&nbsp;MPa UTS &middot; strength-critical</p>
        <p>Nearly twice the strength of 6061 for structural and aerospace parts. Costs more,
        machines fine, avoid welding.</p>
        <ul class="ticks" style="margin-bottom:0">
          <li>UAV arms, airframe brackets, structural ribs</li>
          <li>High-load actuators and linkages</li>
          <li>Fatigue and impact-loaded parts</li>
        </ul>
      </article>
      <article class="card reveal">
        <h3>2024</h3>
        <p class="small" style="margin-bottom:.8em">Fatigue-critical</p>
        <p>Excellent fatigue resistance for aerospace structures, but poor corrosion resistance
        &mdash; usually alodined rather than anodised.</p>
        <ul class="ticks" style="margin-bottom:0">
          <li>Cyclic-load aircraft components</li>
          <li>Alodine or primer-protected assemblies</li>
        </ul>
      </article>
    </div>
    <div class="callout reveal" style="margin-top:24px">
      <p><strong>The anodising detail most articles skip.</strong> 7075 contains copper, and copper
      is the enemy of cosmetic anodising: it produces a yellowish tone and can show a slightly
      mottled finish on thin decorative coatings. Type III hard anodise handles it fine; cosmetic
      Type II black is where 6061 looks better. If your part is an appearance part in black
      anodise, 6061 is usually the smarter pick &mdash; the strength difference is irrelevant on a
      bezel.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="sec-kicker">Stainless steel</span>
      <h2>Stainless steel grades</h2>
      <p>The gap between 303 and 316L is about corrosion and weldability, not strength. Choosing
      wrongly is either money wasted or a part that rusts in service.</p>
    </div>
    <div class="tbl-wrap reveal">
      <table>
        <thead>
          <tr><th>Grade</th><th>Why we reach for it</th><th>Where it fails</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>303</strong></td>
              <td>Best machinability in the stainless family &mdash; ideal for high-volume turned
              fittings and fasteners. Free-cutting, excellent finish.</td>
              <td>Not for marine or chloride exposure; the sulphur addition that makes it
              free-cutting also makes it less corrosion resistant.</td></tr>
          <tr><td><strong>304</strong></td>
              <td>The general-purpose workhorse. Good corrosion resistance, widely available,
              weldable.</td>
              <td>Tougher to machine than 303 &mdash; expect a modest cost premium on turned
              parts. Not ideal for chlorides.</td></tr>
          <tr><td><strong>316L</strong></td>
              <td>Marine and medical. Chloride resistance plus low carbon for welding without
              sensitisation.</td>
              <td>Prices above 304 and machines slower. Over-specified for dry indoor
              applications.</td></tr>
          <tr><td><strong>17-4PH</strong></td>
              <td>High strength after H900 ageing &mdash; aerospace and high-load fixtures where
              304 would be too soft.</td>
              <td>Needs heat treatment to reach spec, so lead time includes the ageing cycle.</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="sec-alt">
  <div class="wrap">
    <div class="grid g2" style="gap:52px;align-items:start">
      <div class="reveal">
        <span class="sec-kicker">Titanium</span>
        <h2>Titanium Grade 2 &amp; Grade 5</h2>
        <p><strong>Grade 5 (Ti-6Al-4V)</strong> for aerospace, medical implants and high-end drone
        hardware &mdash; roughly 950&nbsp;MPa UTS, about 40% lighter than steel at equivalent
        strength.</p>
        <p><strong>Grade 2</strong> where formability and corrosion resistance matter more than
        strength: chemical processing, medical instruments, marine hardware.</p>
        <p>We machine titanium daily &mdash; rigid setups, sharp tooling, flood coolant, slower
        surface speeds &mdash; and we quote it honestly instead of adding a fear margin for a
        material we know well.</p>
        <div class="callout">
          <p><strong>On titanium cost.</strong> The premium is real and mostly unavoidable: material
          cost is 6&ndash;10&times; aluminium, tool life is short, and cutting speeds are a quarter
          of what aluminium tolerates. What is avoidable is a shop padding the quote because it
          would rather not run the job. Ask what the titanium uplift actually reflects.</p>
        </div>
      </div>
      <div class="reveal">
        <span class="sec-kicker">Engineering plastics</span>
        <h2>Engineering plastics</h2>
        <p><strong>PEEK</strong> for medical and aerospace &mdash; machinable, sterilizable,
        chemically inert, and priced accordingly.</p>
        <p><strong>Delrin (POM)</strong> for gears, precision bushings and sliding parts.
        <strong>Nylon</strong> for wear parts and impact resistance. <strong>PTFE</strong> for
        chemical exposure and low-friction surfaces. <strong>PTFE-filled grades</strong> where
        both are needed.</p>
        <div class="callout callout-navy">
          <p><strong>Plastics hold &plusmn;0.05&nbsp;mm reliably.</strong> Tighter needs a design
          review, because thermal movement is physics rather than effort &mdash; a PEEK part grows
          0.05&nbsp;mm per 100&nbsp;mm over a 25&nbsp;&deg;C swing. We will tell you which
          dimensions are achievable and which are a drawing artefact.</p>
        </div>
        <p class="small">Working from a material datasheet someone else supplied?
        <a href="@/blog/aluminum-6061-vs-7075-cnc/">See the practical 6061 vs 7075 comparison &rarr;</a></p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="sec-kicker">Documentation</span>
      <h2>Certificates &amp; traceability</h2>
    </div>
    <div class="grid g3">
      <div class="card reveal">
        <h3>EN 10204 3.1</h3>
        <p>Mill test certificates supplied with metal orders as standard, traceable to heat lot on
        request.</p>
      </div>
      <div class="card reveal">
        <h3>PMI testing</h3>
        <p>Positive material identification available on stainless and titanium, with the report
        attached to the shipment.</p>
      </div>
      <div class="card reveal">
        <h3>RoHS / REACH</h3>
        <p>Declarations available for EU shipments. Plating and anodising processes are
        RoHS-compliant.</p>
      </div>
    </div>
    <div class="cta-band reveal" style="margin-top:44px">
      <div>
        <h2>Not sure which alloy?</h2>
        <p>Send the application description &mdash; loads, environment, finish requirement &mdash;
        and an engineer answers with trade-offs and a price, not a parts catalogue.</p>
      </div>
      <a class="btn btn-primary" href="@/contact/">Ask an engineer</a>
    </div>
  </div>
</section>
"""
