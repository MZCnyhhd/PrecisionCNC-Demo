# PrecisionCNC — Reference Demo Build

A self-built reference site for CNC machining, published so the technical implementation can be
reviewed directly rather than taken on trust.

**Live:** https://mzcnyhhd.github.io/PrecisionCNC-Demo/

## What this is

A **static showcase site**, not a WordPress install and not a client project. It exists to
demonstrate the technical-SEO surface that a WordPress build delivers on a client's own hosting:
canonicals, schema markup, sitemap handling, breadcrumbs, redirect policy, Core Web Vitals
discipline and a working RFQ form.

The WordPress version of this site is deployed separately on the client's hosting (SiteGround +
Cloudflare), with the admin account, database and GSC/GA4 properties handed over at the end.

## What is in the build

| Area | Detail |
| :--- | :--- |
| Pages | 8 indexable sections plus 4 long-form articles = 12 URLs in the sitemap |
| Structured data | Organization, WebSite, LocalBusiness, Service, FAQPage, BreadcrumbList, Article, Blog |
| Crawl files | `sitemap.xml`, `sitemap_index.xml`, `robots.txt`, a real `404.html` served with HTTP 404 |
| Interactivity | Tolerance-to-cost estimator, 6061-vs-7075 alloy selector, RFQ form with file staging + validation |
| Dependencies | **None.** No CDN, no web fonts, no analytics, no cookies. System font stack, ~40 KB of hand-written CSS/JS |
| Compliance surface | Responsive from 390 px, no layout shift by construction, `prefers-reduced-motion` respected |

## Repository layout

```
docs/                  published site — this is what GitHub Pages serves
  assets/style.css     hand-written theme, no framework
  assets/site.js       nav, scroll reveal, both calculators, RFQ validation
  assets/og-cover.svg  social card, generated
  */index.html         one folder per URL, so trailing-slash URLs resolve
  seo-report.html      the technical SEO configuration report for this build
build/
  site_tpl.py          head/nav/footer templates, schema.org nodes
  pages_a.py           Home, Capabilities, Materials
  pages_b.py           Industries, About, Quality, Contact
  pages_blog.py        parses blog_posts.txt and converts a markdown subset
  generate.py          writes the whole of docs/ — idempotent
  smoke_test.py        Playwright runtime test
```

## Rebuilding

```bash
python build/generate.py      # regenerates docs/ from the sources in build/
python build/smoke_test.py    # 40+ runtime assertions; needs playwright installed
```

`generate.py` wipes `docs/` except `assets/` and rebuilds it, so the output tree never accumulates
stale pages. Article bodies live in `../wordpress_seo_bid/site_c_cnc/blog_posts.txt` and are parsed
at build time rather than duplicated.

`smoke_test.py` is the part worth keeping: it loads every page in a real browser and asserts there
are no JS exceptions, that each interactive widget actually changes state when driven, that no
internal link 404s, and that no markdown syntax leaked into rendered output. It caught a genuine
bug during development (a missing DOM node that silently broke the tolerance calculator on two
pages while every page still rendered "fine").

## Notes on honesty

- No fabricated client work. This is a demonstration site and is labelled as one in the site's own
  top banner and in `seo-report.html`.
- No fake testimonials, review markup or aggregate ratings — inventing those is the fastest route
  to a manual action on a real domain.
- No analytics or third-party scripts ship with this build, so reviewing it does not ping anyone.
- Search Console data for this domain, if quoted, is real data from this domain and nothing else.
