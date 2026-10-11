# -*- coding: utf-8 -*-
"""
Blog layer.

The four article bodies already existed as reviewed copy in
``site_c_cnc/blog_posts.txt``. Rather than retype them, this module parses that
file and converts a deliberately small markdown subset to HTML:

  * ``**bold**``            -> <strong>
  * a line that is only bold -> <h2>
  * ``- item`` / ``1. item`` -> <ul> / <ol>
  * consecutive ``| a | b |`` lines -> a table (first row is the header)
  * blank-line separated     -> <p>
"""

import os
import re

SOURCE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "wordpress_seo_bid", "site_c_cnc", "blog_posts.txt")

# Extra metadata the source file does not carry.
META = {
    "5-axis-cnc-machining-when-needed": {
        "date": "2026-07-14",
        "category": "Milling",
        "excerpt": "Five-axis machines are powerful tools, not a quality tier. The three "
                   "situations where 5-axis genuinely saves money, and the ones where 3-axis "
                   "produces the same part for 40% less.",
        "outro": r"""
<div class="callout">
  <p><strong>Want the shop-side answer instead of the general one?</strong> Send the STEP file
  with your critical tolerances marked and we will tell you which process your part actually
  requires &mdash; with a price for both routes where the difference matters. That answer is free;
  the wrong machine choice in production is not.</p>
</div>
<p>More on the machines this applies to: <a href="@/capabilities/#five-axis">5-axis CNC machining
services and envelope &rarr;</a> &middot; <a href="@/contact/">upload files for a quote &rarr;</a></p>
""",
    },
    "aluminum-6061-vs-7075-cnc": {
        "date": "2026-07-28",
        "category": "Materials",
        "excerpt": "The differences that actually matter between 6061-T6 and 7075-T6: strength, "
                   "weldability, corrosion behaviour, and the anodising detail most articles "
                   "skip entirely.",
        "outro": r"""
<div class="callout">
  <p><strong>On the boundary?</strong> We price the same part in both alloys and state the delta.
  On many parts the gap is smaller than customers expect, which turns the decision into
  arithmetic instead of guesswork.</p>
</div>
<p>See also <a href="@/materials/">cnc machining materials in full &mdash; stainless, titanium and
engineering plastics &rarr;</a> and the <a href="@/capabilities/">capabilities these alloys are
machined on &rarr;</a></p>
""",
    },
    "how-to-prepare-cad-files-rfq": {
        "date": "2026-08-11",
        "category": "RFQ",
        "excerpt": "Two customers send identical parts; one gets a precise 24-hour quotation, the "
                   "other gets three days of email ping-pong. What separates them, from the shop "
                   "side of the inbox.",
        "outro": r"""
<div class="callout">
  <p><strong>The checklist before you hit send:</strong> STEP solids &middot; 2D PDF with
  critical tolerances marked &middot; material and finish stated &middot; real quantities &middot;
  target delivery date. Those five lines remove about 90% of quotation friction.</p>
</div>
<p>Ready to send? Use the <a href="@/contact/">RFQ form with file upload &rarr;</a> and read what
travels back with your parts in our <a href="@/quality/">CMM report and inspection workflow
&rarr;</a></p>
""",
    },
    "cnc-machining-tolerances-explained": {
        "date": "2026-08-25",
        "category": "Tolerances",
        "excerpt": "From \u00b10.1 mm down to \u00b10.005 mm: what each tolerance band actually "
                   "costs, why cost scales with risk rather than linearly, and the geometric "
                   "callouts that quietly drive your price.",
        "outro": r"""
<div class="callout">
  <p><strong>Try the numbers yourself.</strong> The tolerance to cost estimator on our
  capabilities page models the relative unit-cost multiplier for each band, including the volume
  factor &mdash; the same logic our quoting desk applies.</p>
</div>
<p>Related: <a href="@/capabilities/">tolerance capability and the machine park behind it
&rarr;</a> &middot; <a href="@/materials/">which materials make tight tolerances harder
&rarr;</a></p>
""",
    },
}

ORDER = [
    "5-axis-cnc-machining-when-needed",
    "aluminum-6061-vs-7075-cnc",
    "cnc-machining-tolerances-explained",
    "how-to-prepare-cad-files-rfq",
]


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def parse_source():
    """Return {slug: {'title':..., 'focus':..., 'body_md':...}}"""
    raw = open(SOURCE, "r", encoding="utf-8").read()
    chunks = re.split(r"^=====\s*POST\s+\d+\s*=====\s*$", raw, flags=re.M)
    posts = {}
    for chunk in chunks[1:]:
        chunk = chunk.strip()
        if not chunk:
            continue
        title_m = re.search(r"^Title:\s*(.+)$", chunk, flags=re.M)
        slug_m = re.search(r"^Slug:\s*(.+)$", chunk, flags=re.M)
        focus_m = re.search(r"^\[Focus Keyword:\s*(.+?)\]\s*$", chunk, flags=re.M)
        if not (title_m and slug_m):
            continue
        slug = slug_m.group(1).strip()
        body_start = chunk.find("\n", chunk.find("Slug:"))
        # body = everything after the focus-keyword line
        fk_end = focus_m.end() if focus_m else body_start
        body = chunk[fk_end:].strip()
        posts[slug] = {
            "title": title_m.group(1).strip(),
            "focus": focus_m.group(1).strip() if focus_m else "",
            "body_md": body,
        }
    return posts


# ---------------------------------------------------------------------------
# Markdown subset -> HTML
# ---------------------------------------------------------------------------

_TABLE_ROW = re.compile(r"^\|(.+)\|\s*$")


def _inline(text):
    text = (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text


def _is_bold_only(line):
    s = line.strip()
    return s.startswith("**") and s.endswith("**") and s.count("**") == 2 and len(s) > 6


def md_to_html(md):
    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)

    def flush_para(buf):
        if buf:
            out.append("<p>" + _inline(" ".join(buf)) + "</p>")
            del buf[:]

    para = []
    while i < n:
        line = lines[i]
        s = line.strip()

        # blank
        if not s:
            flush_para(para)
            i += 1
            continue

        # table
        if _TABLE_ROW.match(s) and i + 1 < n and _TABLE_ROW.match(lines[i + 1].strip()):
            flush_para(para)
            rows = []
            while i < n and _TABLE_ROW.match(lines[i].strip()):
                cells = [c.strip() for c in _TABLE_ROW.match(lines[i].strip()).group(1).split("|")]
                rows.append(cells)
                i += 1
            html = ['<div class="tbl-wrap"><table><thead><tr>']
            for c in rows[0]:
                html.append("<th>" + _inline(c) + "</th>")
            html.append("</tr></thead><tbody>")
            for r in rows[1:]:
                html.append("<tr>")
                for c in r:
                    html.append("<td>" + _inline(c) + "</td>")
                html.append("</tr>")
            html.append("</tbody></table></div>")
            out.append("".join(html))
            continue

        # bold-only line -> h2
        if _is_bold_only(s):
            flush_para(para)
            out.append("<h2>" + _inline(s.strip("*")) + "</h2>")
            i += 1
            continue

        # bullet list
        if s.startswith("- "):
            flush_para(para)
            items = []
            while i < n and lines[i].strip().startswith("- "):
                items.append(_inline(lines[i].strip()[2:]))
                i += 1
            out.append("<ul>" + "".join("<li>" + it + "</li>" for it in items) + "</ul>")
            continue

        # ordered list
        if re.match(r"^\d+\.\s", s):
            flush_para(para)
            items = []
            while i < n and re.match(r"^\d+\.\s", lines[i].strip()):
                items.append(_inline(re.sub(r"^\d+\.\s", "", lines[i].strip())))
                i += 1
            out.append("<ol>" + "".join("<li>" + it + "</li>" for it in items) + "</ol>")
            continue

        para.append(s)
        i += 1

    flush_para(para)
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Page builders
# ---------------------------------------------------------------------------

def article_body(slug):
    posts = parse_source()
    if slug not in posts:
        raise SystemExit("blog slug missing from source: " + slug)
    p = posts[slug]
    m = META[slug]
    html = []
    html.append('<article class="article">')
    html.append('  <div class="article-meta">')
    html.append('    <span class="tag">%s</span>' % m["category"])
    html.append('    <span>Published <time datetime="%s">%s</time></span>' % (m["date"], _human(m["date"])))
    html.append('    <span aria-hidden="true">&middot;</span>')
    html.append('    <span>~%d min read</span>' % _read_minutes(p["body_md"]))
    html.append('  </div>')
    html.append('  <h1>%s</h1>' % _inline(p["title"]))
    html.append(md_to_html(p["body_md"]))
    html.append(m["outro"])
    html.append('  <div class="article-foot">Written by the engineering team at PrecisionCNC. '
                'Every figure quoted comes from parts we have actually cut.</div>')
    html.append('</article>')
    return "\n".join(html)


def _human(iso):
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    y, mo, d = iso.split("-")
    return "%d %s %s" % (int(d), months[int(mo) - 1], y)


def _read_minutes(md):
    return max(3, round(len(md.split()) / 210))


def blog_index_body():
    posts = parse_source()
    rows = []
    for slug in ORDER:
        p = posts[slug]
        m = META[slug]
        rows.append("""
      <li>
        <time datetime="{date}">{human}</time>
        <a href="@/blog/{slug}/">{title}</a>
        <p>{excerpt}</p>
        <p class="small" style="margin-top:6px"><span class="pill">{cat}</span></p>
      </li>""".format(date=m["date"], human=_human(m["date"]), slug=slug,
                      title=_inline(p["title"]), excerpt=_inline(m["excerpt"]),
                      cat=m["category"]))

    return """
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Engineering notes</span>
    <h1>Blog</h1>
    <p>Practical notes from the quoting desk and the shop floor &mdash; process selection,
    material trade-offs and the drawing habits that decide what a part costs. No keyword filler,
    no AI-generated listicles.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="grid g2" style="gap:52px;align-items:start">
      <div class="reveal">
        <ul class="post-list">{rows}
        </ul>
      </div>
      <div class="reveal">
        <div class="tool">
          <div class="tool-head"><span class="dot"></span><h3>Start here</h3></div>
          <div class="tool-body">
            <p>If you are about to send your first RFQ, read the CAD preparation guide first &mdash;
            it is the one that saves the most time.</p>
            <p style="margin-bottom:0"><a class="btn btn-outline btn-block" href="@/blog/how-to-prepare-cad-files-rfq/">How to prepare CAD files for an RFQ</a></p>
            <p style="margin:14px 0 0"><a class="btn btn-outline btn-block" href="@/blog/cnc-machining-tolerances-explained/">Understanding CNC machining tolerances</a></p>
            <p style="margin:14px 0 0"><a class="btn btn-outline btn-block" href="@/blog/aluminum-6061-vs-7075-cnc/">Aluminium 6061 vs 7075</a></p>
            <p style="margin:14px 0 0"><a class="btn btn-outline btn-block" href="@/blog/5-axis-cnc-machining-when-needed/">When you actually need 5-axis</a></p>
          </div>
        </div>
        <div class="callout" style="margin-top:24px">
          <p><strong>Have a question these do not answer?</strong> Send it with your drawing and an
          engineer will reply &mdash; whether or not the answer wins us the order.</p>
          <p style="margin-top:.7em"><a href="@/contact/">Ask an engineer &rarr;</a></p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec-alt">
  <div class="wrap">
    <div class="cta-band reveal">
      <div>
        <h2>Put it into practice</h2>
        <p>Upload a STEP file and a marked-up drawing. Engineering feedback and a priced
        quotation come back within 24 hours.</p>
      </div>
      <a class="btn btn-primary" href="@/contact/">Upload Files &amp; Get a Quote</a>
    </div>
  </div>
</section>
""".format(rows="".join(rows))


def related_body(current_slug):
    posts = parse_source()
    others = [s for s in ORDER if s != current_slug][:3]
    lis = "".join(
        '\n        <li><time datetime="{d}">{h}</time><a href="@/blog/{s}/">{t}</a></li>'.format(
            d=META[s]["date"], h=_human(META[s]["date"]), s=s, t=_inline(posts[s]["title"]))
        for s in others)
    return """
<section class="related">
  <div class="wrap-n">
    <h2 style="margin-bottom:1em">Related reading</h2>
    <ul class="post-list">{lis}
    </ul>
  </div>
</section>
""".format(lis=lis)
