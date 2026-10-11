# -*- coding: utf-8 -*-
"""Body HTML for Industries, About, Quality and Contact."""

INDUSTRIES = r"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Industries</span>
    <h1>Industries We Serve</h1>
    <p>Six sectors account for almost all of our work. Each one has its own documentation
    expectations, material habits and failure modes &mdash; and we have been through the audit
    conversations before.</p>
  </div>
</section>

<section id="medical">
  <div class="wrap">
    <div class="grid g2" style="gap:52px;align-items:start">
      <div class="reveal">
        <span class="sec-kicker">01</span>
        <h2>Medical Devices</h2>
        <p>Prototypes and low-volume production for surgical instruments, trial components and
        device enclosures. We work in 316L and PEEK daily, with passivation and clean packaging
        available on request.</p>
        <p>For design-control audits we provide documented sub-tier process records &mdash; material
        certificates, inspection reports, process parameters and revision traceability.</p>
        <div class="callout">
          <p><strong>An honest boundary.</strong> We do not claim ISO 13485. We support
          ISO&nbsp;13485-certified customers as a documented sub-tier supplier, and we will tell
          you plainly which parts of your quality system we can and cannot satisfy. A supplier
          who overstates their certification is a problem you discover during an audit.</p>
        </div>
        <ul class="ticks">
          <li>316L stainless and PEEK, plus titanium for instruments</li>
          <li>Passivation per ASTM A967 with certification</li>
          <li>Electropolishing coordinated for surgical finish</li>
          <li>Full dimensional report with every order; FAI on request</li>
        </ul>
      </div>
      <div class="reveal">
        <div class="tool">
          <div class="tool-head"><span class="dot"></span><h3>Typical medical work</h3></div>
          <div class="tool-body">
            <div class="spec"><dt>Instruments</dt><dd>Forceps, retractors, trial components, arthroscopic parts</dd></div>
            <div class="spec"><dt>Implant-adjacent</dt><dd>Trial and instrument parts in Grade 5 titanium and 316L</dd></div>
            <div class="spec"><dt>Device enclosures</dt><dd>Machined housings, bezels, brackets, sealing faces</dd></div>
            <div class="spec"><dt>Fluidics</dt><dd>Manifolds, connectors, PEEK insulators and seals</dd></div>
            <div class="spec"><dt>Volumes</dt><dd>1&ndash;500 pieces typical before transfer to moulding or casting</dd></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec-alt" id="aerospace">
  <div class="wrap">
    <div class="grid g2" style="gap:52px;align-items:start">
      <div class="reveal">
        <div class="tool">
          <div class="tool-head"><span class="dot"></span><h3>Typical aerospace &amp; UAV work</h3></div>
          <div class="tool-body">
            <div class="spec"><dt>Structural brackets</dt><dd>5-axis aluminium and titanium, organic geometry, weight-optimised</dd></div>
            <div class="spec"><dt>Airframe parts</dt><dd>UAV arms, motor mounts, gimbal housings, landing gear components</dd></div>
            <div class="spec"><dt>Flight test hardware</dt><dd>One-off instrumented parts with full traceability</dd></div>
            <div class="spec"><dt>Materials</dt><dd>7075-T6, 2024, Ti-6Al-4V, 17-4PH; EN 10204 3.1 certificates</dd></div>
            <div class="spec"><dt>Documentation</dt><dd>AS9102-style FAI, material certs, tooling control records</dd></div>
          </div>
        </div>
      </div>
      <div class="reveal">
        <span class="sec-kicker">02</span>
        <h2>Aerospace &amp; UAV</h2>
        <p>5-axis structural brackets, flight test hardware and UAV frames in 7075 and titanium,
        with FAI documentation, material certificates and tooling control.</p>
        <p>The advantage for development programmes is prototype-to-production continuity: the same
        CAM program and the same fixture that made your three prototypes makes your three hundred
        production parts. No process drift between phases, no re-qualification.</p>
        <ul class="ticks">
          <li>Single-setup 5-axis machining keeps inter-feature position within &plusmn;0.01&nbsp;mm</li>
          <li>AS9102-style first article inspection packages</li>
          <li>Heat-lot traceable material with EN 10204 3.1 certificates</li>
          <li>Tooling retained and controlled so re-runs match the original</li>
        </ul>
        <div class="callout callout-navy">
          <p><strong>Weight is a design decision, not a machining one.</strong> If we can remove
          30&nbsp;grams from a bracket by changing a fillet radius or a pocket depth, the drawing
          review will say so &mdash; before the parts are cut, not after.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="robotics">
  <div class="wrap">
    <div class="grid g2" style="gap:52px;align-items:start">
      <div class="reveal">
        <span class="sec-kicker">03</span>
        <h2>Robotics &amp; Automation</h2>
        <p>Actuator housings, harmonic drive components and custom end-of-arm tooling. In this
        sector, repeatability across batches <em>is</em> the product: batch #200 has to match batch
        #2, dimensionally and cosmetically.</p>
        <p>That means retention tooling, documented process parameters, and anodise colour batches
        managed per order rather than dumped into a common tank.</p>
        <ul class="ticks">
          <li>Harmonic drive and cycloidal component machining to tight position tolerance</li>
          <li>Mill-turn for actuator shafts with cross-ports and flats in one setup</li>
          <li>End-of-arm tooling in 6061 and 7075, bead-blast and anodise finish</li>
          <li>Repeat orders run against the original CAM program and fixture</li>
        </ul>
      </div>
      <div class="reveal">
        <div class="tool">
          <div class="tool-head"><span class="dot"></span><h3>Repeatability by numbers</h3></div>
          <div class="tool-body">
            <div class="spec"><dt>Process control</dt><dd>SPC charts and Cpk reporting on runs above 500 pieces</dd></div>
            <div class="spec"><dt>Fixture control</dt><dd>Tooling numbered, retained and re-used; revisions documented</dd></div>
            <div class="spec"><dt>Anodise colour</dt><dd>Batches tracked per order; samples approved before the run</dd></div>
            <div class="spec"><dt>CAM continuity</dt><dd>Prototype program is the production program &mdash; no silent re-post</dd></div>
            <div class="spec"><dt>Traceability</dt><dd>Part number, revision, heat lot and inspection record archived</dd></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec-alt" id="automotive">
  <div class="wrap">
    <div class="grid g3">
      <div class="reveal">
        <span class="sec-kicker">04</span>
        <h2>Automotive &amp; EV</h2>
        <p>Test rigs, prototype components and charging infrastructure parts. Low-volume work with
        automotive-grade documentation: PPAP-style dimensional reports on request, Cpk data on
        critical characteristics, and revision control that survives your change process.</p>
        <ul class="ticks" style="margin-bottom:0">
          <li>Powertrain and battery-pack test fixtures</li>
          <li>EV charging connector and housing components</li>
          <li>Bracket and mounting hardware in 6061, 6082 and 7075</li>
          <li>Inspection data supplied in your format (CSV, Excel, Q-DAS)</li>
        </ul>
      </div>
      <div class="reveal" id="semiconductor">
        <span class="sec-kicker">05</span>
        <h2>Semiconductor Fixtures</h2>
        <p>Vacuum-compatible aluminium and stainless fixtures, PEEK insulators and clean-finish
        requirements handled at the finishing stage &mdash; targeted bead blasting, dedicated
        tooling for PEEK, and packaging that keeps the finish intact in transit.</p>
        <ul class="ticks" style="margin-bottom:0">
          <li>Vacuum-compatible materials, low outgassing finishes</li>
          <li>PEEK and PTFE insulators, wafer handling components</li>
          <li>Flatness-controlled plate work with CMM mapping</li>
          <li>Clean packaging, gloves-on handling, no bare-metal contact</li>
        </ul>
      </div>
      <div class="reveal" id="electronics">
        <span class="sec-kicker">06</span>
        <h2>Consumer Electronics</h2>
        <p>Appearance parts in anodised aluminium &mdash; bead-blast and anodise cosmetic finishing
        with colour consistency managed per batch. The difference between a good appearance part
        and a rejected one is usually finishing discipline, not machining.</p>
        <ul class="ticks" style="margin-bottom:0">
          <li>6061-T6 bezels, buttons, heat sinks and enclosures</li>
          <li>Bead-blast + Type II anodise with colour matching</li>
          <li>Laser engraving for logos and serial numbers</li>
          <li>First-article cosmetic samples approved before the run</li>
        </ul>
      </div>
    </div>
    <div class="cta-band reveal" style="margin-top:44px">
      <div>
        <h2>Your industry not listed?</h2>
        <p>If it is machined, we have probably made something like it. Send the drawing and an
        engineer will tell you whether it is work we should take &mdash; including when the answer
        is no.</p>
      </div>
      <a class="btn btn-primary" href="@/contact/">Send your drawing</a>
    </div>
  </div>
</section>
"""


ABOUT = r"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">About</span>
    <h1>About PrecisionCNC &mdash; CNC Machine Shop in Dongguan, China</h1>
    <p>Founded in 2011. 45 CNC machining centres across 4,000&nbsp;m&sup2;, 80 employees, of whom
    22 are engineers and quality staff &mdash; the ratio that decides whether a machine shop solves
    problems or just runs parts.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="grid g2" style="gap:52px;align-items:start">
      <div class="reveal">
        <span class="sec-kicker">Who we are</span>
        <h2>The awkward middle territory, on purpose</h2>
        <p>We machine for product development teams and hardware companies across Europe, North
        America and Asia. Not the biggest shop, and deliberately not the cheapest &mdash; the
        clients who stay are the ones who got tired of choosing between two bad options:</p>
        <div class="tbl-wrap" style="margin:1.6rem 0">
          <table>
            <thead><tr><th>Option</th><th>The problem</th></tr></thead>
            <tbody>
              <tr><td><strong>Local prototype shop</strong></td>
                  <td>Fast and communicative, but 3&ndash;5&times; the price once a part needs more
                  than ten pieces.</td></tr>
              <tr><td><strong>Mass-production factory</strong></td>
                  <td>Cheap at volume, rigid about everything else. Prototypes become an
                  afterthought and process continuity breaks between phases.</td></tr>
            </tbody>
          </table>
        </div>
        <p>Our niche sits between them: <strong>prototypes that must match production intent</strong>,
        and low-volume production runs where consistency matters more than the last few percent of
        unit price.</p>
      </div>
      <div class="reveal">
        <div class="tool">
          <div class="tool-head"><span class="dot"></span><h3>At a glance</h3></div>
          <div class="tool-body">
            <div class="spec" style="padding-top:0"><dt>Founded</dt><dd>2011</dd></div>
            <div class="spec"><dt>Location</dt><dd>Dongguan, Guangdong, China</dd></div>
            <div class="spec"><dt>Facility</dt><dd>4,000&nbsp;m&sup2; under one roof</dd></div>
            <div class="spec"><dt>Team</dt><dd>80 staff &mdash; 22 in engineering and quality</dd></div>
            <div class="spec"><dt>Machines</dt><dd>45 CNC machining centres, including 8 five-axis</dd></div>
            <div class="spec"><dt>Certification</dt><dd>ISO 9001:2015</dd></div>
            <div class="spec" style="border-bottom:0"><dt>Main markets</dt><dd>EU &middot; North America &middot; Australia &middot; Singapore</dd></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="sec-kicker">How we differ</span>
      <h2>Four things we do differently from the average machining quote</h2>
      <p>None of these are marketing features. They are the reasons customers stop shopping
      around after the second order.</p>
    </div>
    <div class="grid g2">
      <article class="card reveal">
        <h3><span class="ico"><svg viewBox="0 0 24 24"><path d="M12 3l8 4v5c0 5-3.4 8-8 9-4.6-1-8-4-8-9V7l8-4z"/><path d="M9 12l2 2 4-4"/></svg></span>Engineers answer RFQs</h3>
        <p>Material and tolerance advice is included in the quotation, not upsold as a service.
        If your drawing is over-specified, the reply says so &mdash; with the price difference
        attached.</p>
      </article>
      <article class="card reveal">
        <h3><span class="ico"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9h10M7 13h6"/></svg></span>First-article CMM report, standard</h3>
        <p>Every new part number ships with CMM-verified first-article data. You see the measured
        numbers before committing to volume &mdash; not a certificate of conformance that says
        &ldquo;within specification&rdquo;.</p>
      </article>
      <article class="card reveal">
        <h3><span class="ico"><svg viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h10"/><circle cx="18" cy="17" r="2.5"/></svg></span>No process drift between phases</h3>
        <p>The CAM program and fixture from your prototype run your production batch. No silent
        re-posting, no &ldquo;production version&rdquo; that mysteriously differs from the part you
        validated.</p>
      </article>
      <article class="card reveal">
        <h3><span class="ico"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></svg></span>Honest lead times</h3>
        <p>We would rather lose an order than promise five days and ship in nine. If a date is at
        risk, you hear it from us before you would have found out yourself.</p>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="grid g2" style="gap:52px;align-items:start">
      <div class="reveal">
        <span class="sec-kicker">Working with us</span>
        <h2>What the first order looks like</h2>
        <ol class="steps" style="margin-top:1.6rem">
          <li><b>Send files</b>STEP or IGES for geometry, plus a 2D PDF marking the tolerances that
          matter. Quantity and target date help more than you would expect.</li>
          <li><b>Quote in 24 hours</b>Unit price, price breaks, material and finish
          recommendations, and a delivery date. Any design feedback comes with the quote.</li>
          <li><b>Approval and production</b>Material is drawn against certificates; first article is
          machined and CMM-verified before the run continues.</li>
          <li><b>Inspection and shipping</b>Dimensional report, material certificate and finish
          certification travel with the parts. DDP or DAP, your choice.</li>
        </ol>
      </div>
      <div class="reveal">
        <div class="callout">
          <p><strong>On communication.</strong> Technical questions get answered by the engineer
          who reviewed your part, in writing, within one working day. No account manager relaying
          messages and no &ldquo;let me check with production&rdquo; for three days.</p>
        </div>
        <div class="callout callout-navy">
          <p><strong>On NDAs and IP.</strong> We sign customer NDAs before files are released. We
          do not keep customer designs beyond the retention period your contract specifies, and we
          do not manufacture customer parts for anyone else. Ask for our mutual template if you
          need one.</p>
        </div>
        <p style="margin-top:1.6rem"><a class="btn btn-primary" href="@/contact/">Upload Files &amp; Get a Quote</a>
        &nbsp; <a class="btn btn-outline" href="@/quality/">Quality control in detail</a></p>
      </div>
    </div>
  </div>
</section>
"""


QUALITY = r"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Quality</span>
    <h1>Quality Control &amp; Inspection</h1>
    <p>ISO 9001:2015 certification is the entry ticket, not the differentiator. What matters is
    what happens at the machine and at the CMM &mdash; here is our actual workflow.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="grid g4">
      <div class="card reveal">
        <h3>Incoming</h3>
        <p style="margin:0">Material certificates verified against purchase orders; PMI spot
        checks on stainless and titanium; hardness checks on heat-treated stock before it reaches a
        machine.</p>
      </div>
      <div class="card reveal">
        <h3>In-process</h3>
        <p style="margin:0">First-article inspection on every setup &mdash; the operator cannot run
        production until FAI passes. Probing on mill-turn work; SPC and Cpk reporting above 500
        pieces.</p>
      </div>
      <div class="card reveal">
        <h3>Final</h3>
        <p style="margin:0">100% inspection on critical features, AQL sampling on general
        dimensions. Zeiss CMM for geometric tolerances, optical comparator for profile, roughness
        tester for finish.</p>
      </div>
      <div class="card reveal">
        <h3>Documentation</h3>
        <p style="margin:0">Dimensional report standard with every order. Full FAI package
        (AS9102-style), Cpk data and heat-lot traceability on request.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="sec-kicker">Inspection equipment</span>
      <h2>What we measure with</h2>
      <p>Tolerances are only meaningful relative to the equipment that verifies them. A
      &plusmn;0.005&nbsp;mm claim verified on a caliper is a marketing number, not a measurement.</p>
    </div>
    <div class="tbl-wrap reveal">
      <table>
        <thead>
          <tr><th>Equipment</th><th>Used for</th><th>Practical resolution</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>Zeiss CMM</strong></td>
              <td>Geometric tolerances &mdash; flatness, true position, perpendicularity, profile;
              first articles on all new part numbers</td>
              <td>Sub-micron measurement uncertainty in a temperature-controlled room</td></tr>
          <tr><td><strong>Optical comparator</strong></td>
              <td>Profile features, thread form, small radii and chamfers that are hard to touch-probe</td>
              <td>0.001&nbsp;mm with a good edge</td></tr>
          <tr><td><strong>Height gauge &amp; gauge blocks</strong></td>
              <td>Locating heights, datum offsets, quick verification during a run</td>
              <td>0.001&nbsp;mm</td></tr>
          <tr><td><strong>Thread gauges</strong></td>
              <td>Go / no-go verification of metric, UNC/UNF, NPT and BSPP threads</td>
              <td>Class-of-fit verification</td></tr>
          <tr><td><strong>Surface roughness tester</strong></td>
              <td>Ra verification on sealing faces, bearing bores and cosmetic surfaces</td>
              <td>Ra 0.01&nbsp;&micro;m</td></tr>
          <tr><td><strong>Optical &amp; laser scanning</strong></td>
              <td>Free-form surfaces and full-part deviation maps on request</td>
              <td>Colour deviation map against the nominal CAD</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="grid g2" style="gap:52px;align-items:start">
      <div class="reveal">
        <span class="sec-kicker">Documentation</span>
        <h2>What ships with your parts</h2>
        <p style="margin-bottom:1em"><strong>Standard with every order:</strong></p>
        <ul class="ticks">
          <li>Dimensional inspection report against the drawing</li>
          <li>Material certificate per EN 10204 3.1 (metal orders)</li>
          <li>Finish certification where a finish was specified</li>
          <li>Packing list with quantity and part number</li>
        </ul>
        <p style="margin:1.6em 0 1em"><strong>Available on request:</strong></p>
        <ul class="ticks">
          <li>Full FAI package, AS9102-style</li>
          <li>Cpk / SPC data on production characteristics</li>
          <li>Heat-lot traceability and PMI reports</li>
          <li>Inspection data in your format (CSV, Excel, Q-DAS)</li>
          <li>Certificate of conformance with authorised signature</li>
        </ul>
      </div>
      <div class="reveal">
        <span class="sec-kicker">Non-conformance</span>
        <h2>When something goes wrong</h2>
        <div class="callout" style="margin-top:1.2rem">
          <p><strong>Real talk.</strong> With 45 machines running mixed prototypes, things
          occasionally go wrong. Our non-conformance process is why customers stay.</p>
        </div>
        <ol class="steps" style="margin-top:1.6rem">
          <li><b>You hear it from us first</b>Before you find it. If we catch a problem in final
          inspection, the email goes out the same day &mdash; not after you chase a late
          shipment.</li>
          <li><b>Disposition within 24 hours</b>Rework, replacement or credit, decided and
          communicated in one working day.</li>
          <li><b>Documented root cause</b>Written cause analysis with the corrective action, sent
          with the replacement parts.</li>
          <li><b>Updated reports</b>New first-article data on whatever comes out of the fix &mdash;
          you do not have to ask for it.</li>
        </ol>
        <div class="callout callout-navy">
          <p><strong>What we do not do:</strong> ship a non-conforming batch and hope it passes
          incoming inspection downstream. It costs us an order, but it costs you a production line.</p>
        </div>
        <p style="margin-top:1.6rem"><a class="btn btn-primary" href="@/contact/">Request our quality manual</a></p>
      </div>
    </div>
  </div>
</section>
"""


CONTACT = r"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Request a quote</span>
    <h1>Upload Files &amp; Get a Quote</h1>
    <p>Send STEP/IGES/STP files, plus a 2D PDF drawing marking tolerances and finishes if you
    have one. Within 24 hours you receive unit pricing at your quantity, price breaks at higher
    volumes, material and finish recommendations, and an honest delivery date.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="grid g2" style="gap:52px;align-items:start">
      <div class="reveal">
        <div class="tool">
          <div class="tool-head"><span class="dot"></span><h3>Request for quotation</h3></div>
          <div class="tool-body">
            <form id="rfq-form" novalidate>
              <div class="row2">
                <div class="field">
                  <label for="rfq-name">Your name <span class="req">*</span></label>
                  <input type="text" id="rfq-name" name="name" required autocomplete="name">
                </div>
                <div class="field">
                  <label for="rfq-company">Company</label>
                  <input type="text" id="rfq-company" name="company" autocomplete="organization">
                </div>
              </div>
              <div class="row2">
                <div class="field">
                  <label for="rfq-email">Work email <span class="req">*</span></label>
                  <input type="email" id="rfq-email" name="email" required autocomplete="email">
                </div>
                <div class="field">
                  <label for="rfq-country">Country / region</label>
                  <select id="rfq-country" name="country">
                    <option value="">Select&hellip;</option>
                    <option>Germany</option><option>Netherlands</option><option>United Kingdom</option>
                    <option>France</option><option>Italy</option><option>Sweden</option>
                    <option>United States</option><option>Canada</option><option>Australia</option>
                    <option>Singapore</option><option>Japan</option><option>Other</option>
                  </select>
                </div>
              </div>
              <div class="field">
                <label>CAD files <span class="req">*</span>
                  <span class="hint">&mdash; STEP / IGES / STP / PDF, up to 5 files, 20&nbsp;MB each</span></label>
                <div class="drop" id="rfq-drop" role="button" tabindex="0"
                     aria-label="Upload CAD files">
                  <svg viewBox="0 0 24 24"><path d="M12 16V4"/><path d="M7 9l5-5 5 5"/><path d="M4 17v2a2 2 0 002 2h12a2 2 0 002-2v-2"/></svg>
                  <b>Drop your STEP files here</b>
                  <span>or click to browse &mdash; nothing leaves your browser on this demo build</span>
                </div>
                <input type="file" id="rfq-files" multiple hidden
                       accept=".step,.stp,.iges,.igs,.pdf,.sldprt,.x_t">
                <ul class="filelist" id="rfq-filelist"></ul>
              </div>
              <div class="row2">
                <div class="field">
                  <label for="rfq-qty">Quantity <span class="req">*</span></label>
                  <input type="number" id="rfq-qty" name="quantity" min="1" value="1" required>
                </div>
                <div class="field">
                  <label for="rfq-date">Target delivery date</label>
                  <input type="date" id="rfq-date" name="target_date">
                </div>
              </div>
              <div class="field">
                <label for="rfq-notes">Material, tolerance &amp; finish requirements</label>
                <textarea id="rfq-notes" name="notes"
                  placeholder="e.g. 7075-T6, critical bores at &#177;0.01 mm, Type II black anodise, need FAI report"></textarea>
              </div>
              <button class="btn btn-primary btn-block" type="submit">Submit RFQ</button>
              <div id="rfq-status" class="form-note">Engineering review, quotation back within 24
              hours. We sign NDAs before files are released &mdash; ask if you need one.</div>
            </form>
          </div>
        </div>
      </div>

      <div class="reveal">
        <span class="sec-kicker">Direct contact</span>
        <h2>Talk to an engineer</h2>
        <div class="spec" style="padding-top:0"><dt>Email</dt><dd><span class="mono">quote@precisioncnc-tech.com</span></dd></div>
        <div class="spec"><dt>WhatsApp</dt><dd><span class="mono">+86 137 XXXX XXXX</span></dd></div>
        <div class="spec"><dt>WeChat</dt><dd>Available on request for existing customers</dd></div>
        <div class="spec" style="border-bottom:0"><dt>Hours</dt><dd>Mon&ndash;Sat, 08:30&ndash;18:30 GMT+8</dd></div>

        <h3 style="margin-top:2em">Factory</h3>
        <p>No.18 Hengli Industrial Rd<br>Dongguan, Guangdong<br>China</p>

        <div class="callout">
          <p><strong>What to send for the fastest quote.</strong> A STEP file with watertight
          solids, a 2D PDF with critical tolerances marked, material and finish stated, real
          quantities, and a target date. Five lines of information removes about 90% of quotation
          friction.</p>
          <p style="margin-top:.8em"><a href="@/blog/how-to-prepare-cad-files-rfq/">Read the full RFQ
          preparation guide &rarr;</a></p>
        </div>

        <div class="callout callout-navy">
          <p><strong>About this page.</strong> This is a reference demo build &mdash; a static
          showcase site, not a live shop. The form above validates in your browser and transmits
          nothing, because there is no server behind it. On the production WordPress build the
          same form is Fluent Forms with file upload, wired to WP Mail SMTP so submissions land in
          the shop inbox with the STEP file attached.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="sec-kicker">Before you send</span>
      <h2>Five things that decide your quote price</h2>
    </div>
    <div class="grid g3">
      <div class="card reveal">
        <h3>1. File format</h3>
        <p>STEP or IGES. Native CAD files cause version-mismatch import errors, and STL alone needs
        remodelling before it can be quoted.</p>
      </div>
      <div class="card reveal">
        <h3>2. Marked tolerances</h3>
        <p>Flag the functional dimensions and let the rest ride at ISO 2768-m. This one habit
        typically saves 15&ndash;25% on precision parts.</p>
      </div>
      <div class="card reveal">
        <h3>3. Thread callouts</h3>
        <p>Size, pitch, depth and class on the drawing. &ldquo;Add threads where needed&rdquo; is
        the single most common cause of quote delay.</p>
      </div>
      <div class="card reveal">
        <h3>4. Real quantities</h3>
        <p>&ldquo;5 now, 50 in Q3&rdquo; lets us design the fixture for the transition. Fixtures
        designed on prototype day make production day cheap.</p>
      </div>
      <div class="card reveal">
        <h3>5. Material and finish</h3>
        <p>Alloy, temper, anodise type and colour, surface roughness target. One sentence prevents
        one re-make.</p>
      </div>
      <div class="card reveal">
        <h3>Not sure?</h3>
        <p>Send what you have. An engineer will tell you what is missing and whether the gap
        actually affects the price &mdash; usually it does not.</p>
      </div>
    </div>
  </div>
</section>
"""
