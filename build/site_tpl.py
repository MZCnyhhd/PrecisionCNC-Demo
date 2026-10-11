# -*- coding: utf-8 -*-
"""
Site template layer for the PrecisionCNC reference demo build.

Everything is emitted as fully static, self-contained HTML: no CDN, no web
fonts, no external requests. That matters for two reasons — it survives the
GFW, and it makes the technical-SEO structure directly inspectable in
View Source.
"""

BASE_URL = "https://mzcnyhhd.github.io/PrecisionCNC-Demo"
BRAND = "PrecisionCNC"
BRAND_SUB = "Precision Machining"

# (label, absolute path) — Home is the brand mark, Contact is the header CTA
NAV = [
    ("Capabilities", "/capabilities/"),
    ("Materials", "/materials/"),
    ("Industries", "/industries/"),
    ("Quality", "/quality/"),
    ("About", "/about/"),
    ("Blog", "/blog/"),
]

FOOTER_LINKS = {
    "Capabilities": [
        ("5-Axis CNC Milling", "/capabilities/#five-axis"),
        ("CNC Turning & Mill-Turn", "/capabilities/#turning"),
        ("Tolerances & Precision", "/capabilities/#tolerances"),
        ("Materials", "/materials/"),
        ("Finishing", "/capabilities/#finishing"),
        ("Quality & Inspection", "/quality/"),
    ],
    "Industries": [
        ("Medical Devices", "/industries/#medical"),
        ("Aerospace & UAV", "/industries/#aerospace"),
        ("Robotics & Automation", "/industries/#robotics"),
        ("Automotive & EV", "/industries/#automotive"),
        ("Semiconductor Fixtures", "/industries/#semiconductor"),
        ("Consumer Electronics", "/industries/#electronics"),
    ],
    "Company": [
        ("About PrecisionCNC", "/about/"),
        ("Blog", "/blog/"),
        ("Upload Files & Get a Quote", "/contact/"),
        ("Technical SEO Report", "/seo-report.html"),
        ("Sitemap (XML)", "/sitemap.xml"),
        ("Robots.txt", "/robots.txt"),
    ],
}

# Inline SVG logo — no image file, no external request.
LOGO_SVG = """<svg class="brand-mark" viewBox="0 0 40 40" role="img" aria-label="PrecisionCNC logo">
<rect width="40" height="40" rx="9" fill="#0B2545"/>
<path d="M11 29V11h7.4a6.1 6.1 0 0 1 0 12.2H15.4V29H11z" fill="#fff"/>
<circle cx="27.5" cy="24.5" r="3.6" fill="none" stroke="#E8590C" stroke-width="2.4"/>
</svg>"""


def rel(path, depth):
    """Resolve a site-absolute path to a page-relative URL."""
    if path.startswith("http"):
        return path
    if depth <= 0:
        return path.lstrip("/") or "./"
    if path == "/":
        return "../" * depth
    return ("../" * depth) + path.lstrip("/")


def abs_url(path):
    if path.startswith("http"):
        return path
    return BASE_URL + path


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


# ---------------------------------------------------------------------------
# Head / chrome
# ---------------------------------------------------------------------------

def render_head(depth, title, description, canonical_path, schema=None,
                og_type="website", robots="index, follow, max-image-preview:large"):
    og_image = abs_url("/assets/og-cover.svg")
    schemas = schema if isinstance(schema, list) else ([schema] if schema else [])
    schema_html = ""
    for s in schemas:
        schema_html += ('\n  <script type="application/ld+json">'
                        + _json(s) + '</script>')
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <meta name="robots" content="{robots}">
  <link rel="canonical" href="{abs_url(canonical_path)}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="{BRAND}">
  <meta property="og:locale" content="en_US">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{abs_url(canonical_path)}">
  <meta property="og:image" content="{og_image}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(description)}">
  <meta name="theme-color" content="#0B2545">
  <link rel="icon" href="{rel('/assets/favicon.svg', depth)}" type="image/svg+xml">
  <link rel="stylesheet" href="{rel('/assets/style.css', depth)}">{schema_html}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="demo-strip">
  Reference demo build &middot; self-built showcase site, portfolio review only &middot;
  <a href="{rel('/seo-report.html', depth)}">Technical SEO configuration report &rarr;</a>
</div>
"""


def render_header(depth, active=""):
    links = ""
    for label, path in NAV:
        cur = ' aria-current="page"' if path == active else ""
        links += f'\n        <a href="{rel(path, depth)}"{cur}>{label}</a>'
    return f"""<header class="site-header">
  <div class="wrap header-in">
    <a class="brand" href="{rel('/', depth)}">
      {LOGO_SVG}
      <span>{BRAND}<small>{BRAND_SUB}</small></span>
    </a>
    <button class="burger" type="button" aria-label="Toggle navigation" aria-expanded="false" aria-controls="site-nav">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav" id="site-nav" aria-label="Main">{links}
        <a class="nav-cta" href="{rel('/contact/', depth)}">Get a Quote</a>
    </nav>
  </div>
</header>
"""


def render_footer(depth):
    cols = ""
    for heading, items in FOOTER_LINKS.items():
        lis = "".join(f'\n            <li><a href="{rel(p, depth)}">{esc(t)}</a></li>'
                      for t, p in items)
        cols += f"""
        <div>
          <h4>{heading}</h4>
          <ul>{lis}
          </ul>
        </div>"""
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-about">
        <a class="brand" href="{rel('/', depth)}">
          {LOGO_SVG}
          <span>{BRAND}<small>{BRAND_SUB}</small></span>
        </a>
        <p>Custom CNC machining \u2014 5-axis milling, turning and mill-turn work for prototypes and
        low-volume production. Dongguan, China. Engineered quotes in 24 hours.</p>
      </div>{cols}
    </div>
  </div>
  <div class="wrap">
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> {BRAND} Tech Co., Ltd. \u2014 reference demo build.</span>
      <span>Static HTML/CSS/JS &middot; no CDN, no trackers, no cookies</span>
    </div>
  </div>
</footer>
<script src="{rel('/assets/site.js', depth)}"></script>
</body>
</html>
"""


def render_crumbs(depth, trail):
    """trail: list of (label, absolute_path|None)"""
    lis = ""
    for i, (label, path) in enumerate(trail):
        if path and i < len(trail) - 1:
            lis += f'\n      <li><a href="{rel(path, depth)}">{esc(label)}</a></li>'
        else:
            lis += f'\n      <li><span aria-current="page">{esc(label)}</span></li>'
    return f"""<nav class="crumbs" aria-label="Breadcrumb">
  <div class="wrap">
    <ol>{lis}
    </ol>
  </div>
</nav>
"""


def breadcrumb_schema(trail):
    items = []
    for i, (label, path) in enumerate(trail, start=1):
        items.append({
            "@type": "ListItem",
            "position": i,
            "name": label,
            "item": abs_url(path) if path else BASE_URL + "/",
        })
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": items}


# ---------------------------------------------------------------------------
# Shared schema.org nodes
# ---------------------------------------------------------------------------

ORG_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": BASE_URL + "/#organization",
    "name": "PrecisionCNC Tech Co., Ltd.",
    "alternateName": "PrecisionCNC",
    "url": BASE_URL + "/",
    "logo": {"@type": "ImageObject", "url": abs_url("/assets/og-cover.svg"),
             "width": 1200, "height": 630},
    "description": "CNC machining supplier offering 5-axis milling, turning and mill-turn "
                   "work for prototypes and low-volume production in aluminium, stainless "
                   "steel, titanium and engineering plastics.",
    "foundingDate": "2011",
    "numberOfEmployees": {"@type": "QuantitativeValue", "value": 80},
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "No.18 Hengli Industrial Rd",
        "addressLocality": "Dongguan",
        "addressRegion": "Guangdong",
        "addressCountry": "CN",
    },
    "contactPoint": [{
        "@type": "ContactPoint",
        "contactType": "sales",
        "email": "quote@precisioncnc-tech.com",
        "availableLanguage": ["en", "zh"],
        "areaServed": ["EU", "US", "CA", "AU", "SG"],
    }],
    "knowsAbout": ["CNC machining", "5-axis milling", "CNC turning",
                   "rapid prototyping", "CMM inspection", "GD&T"],
}

WEBSITE_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": BASE_URL + "/#website",
    "url": BASE_URL + "/",
    "name": "PrecisionCNC | 5-Axis CNC Machining & Custom Parts",
    "publisher": {"@id": BASE_URL + "/#organization"},
    "inLanguage": "en",
}

LOCALBIZ_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "@id": BASE_URL + "/#localbusiness",
    "name": "PrecisionCNC Tech Co., Ltd.",
    "image": abs_url("/assets/og-cover.svg"),
    "url": BASE_URL + "/",
    "email": "quote@precisioncnc-tech.com",
    "priceRange": "$$",
    "address": ORG_SCHEMA["address"],
    "geo": {"@type": "GeoCoordinates", "latitude": 23.0207, "longitude": 113.7518},
    "openingHoursSpecification": [{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday",
                      "Friday", "Saturday"],
        "opens": "08:30", "closes": "18:30",
    }],
}

SERVICE_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "Service",
    "serviceType": "CNC machining services",
    "provider": {"@id": BASE_URL + "/#organization"},
    "areaServed": {"@type": "Place", "name": "Worldwide"},
    "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "CNC machining capabilities",
        "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service",
             "name": "5-Axis CNC Milling", "url": abs_url("/capabilities/")}},
            {"@type": "Offer", "itemOffered": {"@type": "Service",
             "name": "CNC Turning & Mill-Turn", "url": abs_url("/capabilities/")}},
            {"@type": "Offer", "itemOffered": {"@type": "Service",
             "name": "Prototype CNC Machining", "url": abs_url("/capabilities/")}},
            {"@type": "Offer", "itemOffered": {"@type": "Service",
             "name": "Low-Volume Production", "url": abs_url("/capabilities/")}},
        ],
    },
}

FAQ_HOME = [
    ("What is your minimum order quantity?",
     "One piece. Prototypes from a single part are how most of our customer "
     "relationships start \u2014 it is the cheapest place to test a machine shop."),
    ("How fast can I get a quote?",
     "Within 24 hours of receiving a STEP file and a 2D drawing. The reply "
     "includes unit pricing, price breaks at higher volumes, material and finish "
     "recommendations, and a delivery date we intend to keep."),
    ("Do you work from drawings only, or do you need 3D CAD?",
     "We need 3D geometry to quote accurately. STEP or IGES is ideal. Export "
     "STEP from whatever CAD package you use rather than sending native files."),
    ("Which countries do you ship to?",
     "Most of our work goes to the EU, North America, Australia and Singapore. "
     "We quote DDP and DAP terms depending on your preference."),
    ("Do you sign NDAs?",
     "Yes \u2014 send yours and we will return a signed copy before you release "
     "files, or ask us for a mutual NDA template."),
]

FAQ_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in FAQ_HOME
    ],
}


def _json(obj):
    import json
    return json.dumps(obj, ensure_ascii=False, indent=2)
