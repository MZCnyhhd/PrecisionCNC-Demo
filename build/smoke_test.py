# -*- coding: utf-8 -*-
"""
Runtime smoke test for the generated site.

Catches what static inspection cannot: JS exceptions, broken interactive
widgets, dead internal links and missing meta. Run after every generate.py.
"""

import os
import sys
import glob
import http.server
import socketserver
import threading
import urllib.parse
from playwright.sync_api import sync_playwright

DOCS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
PORT = 8099
BASE = "http://127.0.0.1:%d/" % PORT

failures = []
notes = []


def fail(msg):
    failures.append(msg)
    print("  FAIL  " + msg)


def ok(msg):
    print("  ok    " + msg)


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=DOCS, **kw)

    def log_message(self, *a):
        pass


def serve():
    handler = QuietHandler
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), handler)
    httpd.allow_reuse_address = True
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    return httpd


def page_url(rel_path):
    if rel_path == "index.html":
        return BASE
    if rel_path.endswith("index.html"):
        return BASE + rel_path[:-len("index.html")]
    return BASE + rel_path


def main():
    httpd = serve()
    html_files = sorted(
        os.path.relpath(p, DOCS).replace(os.sep, "/")
        for p in glob.glob(os.path.join(DOCS, "**", "*.html"), recursive=True))

    console_errors = []
    page_errors = []

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        ctx = browser.new_context(viewport={"width": 1440, "height": 900})
        page = ctx.new_page()
        page.on("console", lambda m: console_errors.append((current[0], m.text))
                if m.type == "error" else None)
        page.on("pageerror", lambda e: page_errors.append((current[0], str(e))))

        current = ["?"]

        print("\n=== 1. load every page, catch JS errors / missing meta ===")
        for rel in html_files:
            current[0] = rel
            before_c, before_p = len(console_errors), len(page_errors)
            resp = page.goto(page_url(rel), wait_until="load")
            page.wait_for_timeout(120)

            if resp is None or resp.status != 200:
                fail("%s -> HTTP %s" % (rel, resp.status if resp else "none"))
                continue
            if len(page_errors) > before_p:
                fail("%s raised a JS exception: %s" % (rel, page_errors[-1][1][:160]))
            if len(console_errors) > before_c:
                fail("%s logged a console error: %s" % (rel, console_errors[-1][1][:160]))

            h1 = page.locator("h1").count()
            if h1 != 1:
                fail("%s has %d <h1> elements (expected 1)" % (rel, h1))
            canonical = page.get_attribute('link[rel="canonical"]', "href")
            if not canonical:
                fail("%s missing canonical" % rel)
            title = page.title()
            if not title or len(title) < 12:
                fail("%s has a weak <title>: %r" % (rel, title))
            if not page.get_attribute('meta[name="description"]', "content"):
                fail("%s missing meta description" % rel)
            # stylesheet actually applied?
            bg = page.evaluate("getComputedStyle(document.body).backgroundColor")
            if bg in ("rgba(0, 0, 0, 0)", ""):
                fail("%s stylesheet did not apply (body background is %s)" % (rel, bg))
            ok("%-52s %s" % (rel, title[:46]))

        print("\n=== 2. internal link integrity ===")
        current[0] = "all pages"
        seen = set()
        for rel in html_files:
            page.goto(page_url(rel), wait_until="load")
            hrefs = page.eval_on_selector_all("a[href]", "els => els.map(e => e.getAttribute('href'))")
            for h in hrefs:
                if not h or h.startswith(("http", "mailto:", "tel:", "#", "//")):
                    continue
                target = h.split("#")[0]
                if not target:
                    continue
                full = urllib.parse.urljoin(page_url(rel), target)
                path = urllib.parse.urlparse(full).path.lstrip("/")
                if path == "" or path.endswith("/"):
                    path += "index.html"
                if path not in seen:
                    seen.add(path)
                    if not os.path.isfile(os.path.join(DOCS, path)):
                        fail("%s links to missing file: %s" % (rel, h))
        ok("checked %d distinct internal targets" % len(seen))

        print("\n=== 3. tolerance / cost estimator (home) ===")
        current[0] = "index.html#tol-tool"
        page.goto(BASE, wait_until="load")
        out = page.inner_text("#tol-out")
        first = page.inner_text("#tol-cost")
        page.locator("#tol-range").fill("4")
        page.wait_for_timeout(120)
        last = page.inner_text("#tol-cost")
        label = page.inner_text("#tol-band-label")
        if first == last:
            fail("tolerance slider did not change the cost output (stuck at %s)" % first)
        else:
            ok("slider 0.1mm -> 0.005mm moves cost %s -> %s (%s)" % (first, last, label))
        if "0.005" not in label:
            fail("band label did not update to tightest band: %r" % label)
        # volume factor path
        page.locator("#tol-qty").fill("500")
        page.wait_for_timeout(120)
        vol = page.inner_text("#tol-cost")
        if vol == last:
            fail("quantity input did not affect the volume factor")
        else:
            ok("quantity 10 -> 500 changes cost %s -> %s" % (last, vol))
        page.locator(".chip[data-idx='1']").click()
        page.wait_for_timeout(120)
        if "0.05" not in page.inner_text("#tol-band-label"):
            fail("band chip click did not update the tool")
        else:
            ok("band chips drive the slider")
        if not out.strip():
            fail("tolerance result panel is empty")

        print("\n=== 4. alloy selector (materials) ===")
        current[0] = "materials/index.html#alloy-tool"
        page.goto(BASE + "materials/", wait_until="load")
        qcount = page.locator("#alloy-form .field").count()
        if qcount != 5:
            fail("alloy selector rendered %d questions (expected 5)" % qcount)
        else:
            ok("5 criteria rendered")
        default = page.inner_text("#alloy-out")
        # answer: welded = yes, everything else no -> should land on 6061
        page.locator('.chip[data-q="weld"][data-val="yes"]').click()
        page.wait_for_timeout(120)
        after = page.inner_text("#alloy-out")
        if after == default:
            fail("alloy selector output did not change after answering")
        elif "6061" not in after:
            fail("welded part should recommend 6061, got: %s" % after[:90].replace("\n", " "))
        else:
            ok("weld=yes -> 6061 recommendation")
        page.locator('.chip[data-q="load"][data-val="yes"]').click()
        page.locator('.chip[data-q="fatig"][data-val="yes"]').click()
        page.wait_for_timeout(120)
        after2 = page.inner_text("#alloy-out")
        if "7075" not in after2:
            fail("two 7075 drivers should outvote one 6061 driver, got: %s"
                 % after2[:90].replace("\n", " "))
        else:
            ok("load+fatigue=yes -> 7075 recommendation")

        print("\n=== 5. RFQ form validation (contact) ===")
        current[0] = "contact/index.html#rfq-form"
        page.goto(BASE + "contact/", wait_until="load")
        page.locator("#rfq-form button[type=submit]").click()
        page.wait_for_timeout(150)
        msg = page.inner_text("#rfq-status")
        if "required" not in msg.lower():
            fail("empty submit did not surface a validation message: %r" % msg[:80])
        else:
            ok("empty submit blocked with a validation message")
        page.fill("#rfq-name", "Ana Weber")
        page.fill("#rfq-email", "ana@example.com")
        page.fill("#rfq-qty", "250")
        page.locator("#rfq-form button[type=submit]").click()
        page.wait_for_timeout(200)
        msg2 = page.inner_text("#rfq-status")
        if "static" not in msg2.lower() and "demonstration" not in msg2.lower():
            fail("valid submit did not reach the success state: %r" % msg2[:90])
        else:
            ok("valid submit reaches success state and states it is a static build")
        if "5" not in msg2:
            notes.append("success message no longer states the required-field count")
        # file staging
        page.set_input_files("#rfq-files", {
            "name": "bracket-rev-c.step", "mimeType": "application/octet-stream",
            "buffer": b"ISO-10303-21;HEADER;"})
        page.wait_for_timeout(200)
        if page.locator("#rfq-filelist li").count() != 1:
            fail("file staging did not add a list row")
        else:
            ok("file staging renders the queued file (name + size)")
        page.locator("#rfq-filelist .rm").click()
        page.wait_for_timeout(120)
        if page.locator("#rfq-filelist li").count() != 0:
            fail("remove button did not clear the staged file")
        else:
            ok("remove button clears the staged file")

        print("\n=== 6. mobile navigation ===")
        current[0] = "mobile nav"
        mob = ctx.new_page()
        mob.set_viewport_size({"width": 390, "height": 844})
        mob.goto(BASE, wait_until="load")
        if mob.locator("#site-nav").is_visible():
            fail("mobile nav is visible before the burger is tapped")
        else:
            ok("mobile nav starts collapsed")
        mob.locator(".burger").click()
        mob.wait_for_timeout(150)
        if not mob.locator("#site-nav").is_visible():
            fail("burger tap did not open the mobile nav")
        else:
            ok("burger opens the nav")
        mob.locator("#site-nav a", has_text="Capabilities").first.click()
        mob.wait_for_url("**/capabilities/**", timeout=4000)
        ok("mobile nav link navigates to %s" % mob.url.replace(BASE, "/"))
        mob.close()

        print("\n=== 7. rendering artefacts ===")
        current[0] = "render"
        page.set_viewport_size({"width": 1440, "height": 900})
        page.goto(BASE, wait_until="load")
        page.wait_for_timeout(400)
        overflow = page.evaluate(
            "() => document.documentElement.scrollWidth - document.documentElement.clientWidth")
        if overflow > 4:
            fail("horizontal overflow on desktop: %dpx" % overflow)
        else:
            ok("no horizontal overflow at 1440px")
        page.set_viewport_size({"width": 390, "height": 844})
        page.wait_for_timeout(300)
        overflow_m = page.evaluate(
            "() => document.documentElement.scrollWidth - document.documentElement.clientWidth")
        if overflow_m > 4:
            fail("horizontal overflow on mobile: %dpx" % overflow_m)
        else:
            ok("no horizontal overflow at 390px")
        # raw markdown leaking into rendered output?
        body_text = page.inner_text("body")
        for marker in ["**", "@/", "&amp;", "&plusmn;"]:
            if marker in body_text:
                fail("raw markup leaked into rendered text: %r" % marker)
        ok("no raw markup leakage on home")

        print("\n=== 8. blog articles ===")
        for slug in ["5-axis-cnc-machining-when-needed", "aluminum-6061-vs-7075-cnc",
                     "how-to-prepare-cad-files-rfq", "cnc-machining-tolerances-explained"]:
            current[0] = "blog/" + slug
            page.goto(BASE + "blog/%s/" % slug, wait_until="load")
            body_text = page.inner_text("body")
            if "**" in body_text:
                fail("%s: markdown asterisks rendered as literal text" % slug)
            h2 = page.locator("article h2").count()
            if h2 < 3:
                fail("%s: only %d <h2> sections parsed" % (slug, h2))
            tbl = page.locator("article table").count()
            ok("%s: %d sections, %d table(s)" % (slug, h2, tbl))
        # table specifically for the comparison post
        page.goto(BASE + "blog/aluminum-6061-vs-7075-cnc/", wait_until="load")
        if page.locator("article table tbody tr").count() < 5:
            fail("6061 vs 7075 decision table did not parse into a real table")
        else:
            ok("6061 vs 7075 decision table parsed with %d rows"
               % page.locator("article table tbody tr").count())

        browser.close()

    httpd.shutdown()

    print("\n=== console noise summary ===")
    if console_errors:
        for p, m in console_errors[:10]:
            print("   console error on %s: %s" % (p, m[:150]))
    else:
        print("   no console errors on any page")
    print("   no page exceptions" if not page_errors else "   %d page exceptions" % len(page_errors))

    print("\n=== RESULT ===")
    if failures:
        print("%d FAILURE(S)" % len(failures))
        for f in failures:
            print("  - " + f)
        sys.exit(1)
    print("all smoke checks passed")
    for n in notes:
        print("  note: " + n)


if __name__ == "__main__":
    main()
