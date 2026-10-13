# Local acceptance report

Verified 13 October 2026 against the minified production output. Verdict: **PASS for local delivery**. No local blockers remain.

| Check | Result | Evidence |
|---|---|---|
| Production build | PASS | Hugo extended 0.164; 15 HTML documents |
| Homepage structure and inventory | PASS | Required sections and order, timeline, all Explore destinations |
| Rendered content and schema | PASS | Render audit; 22 parseable JSON-LD blocks; price and review-count validation |
| Responsive layout | PASS | Nine page types at six widths from 320 to 1440 pixels |
| Hero contrast and fold | PASS | Homepage and both landing pages, desktop and mobile |
| Flat design and dark-background text | PASS | Design and computed contrast audits |
| Galleries | PASS | Three tours, 15 gallery photos, no cross-tour duplicates |
| Guide widget placement | PASS | All four guide articles |
| Prose ratings and price basis | PASS | Catalogue-consistent ratings and per-person prices |
| Analytics in head | PASS | Exactly one loader on each of 15 HTML pages |
| Partner ID | PASS | Configuration, JavaScript and widgets use 1MSALBX |
| Campaign | PASS | frascatiwinetours throughout |
| Static booking fallbacks | PASS | 28 direct product URLs; runtime destinations and attribution checked |
| Internal links | PASS | 556 internal hrefs examined, zero dead links; inbound-link audit passed |
| Browser behavior | PASS | Fonts, hydrated booking widget, FAQ toggles and mobile menu at 1440, 768 and 390 pixels; no captured JavaScript errors |
| JavaScript disabled | PASS | Heading visible; booking fallback URLs retained |
| Live-domain links and hosting rules | N/A | Site not deployed; checks cover local output only |

Raw reports and screenshots are in `research/qa/`. The source register and review provenance are in `research/`. Structured data was validated locally; an externally hosted Google Rich Results run is not claimed.

To repeat the site's attribution checks:

```bash
./scripts/build.sh
python3 scripts/verify-site.py
```

The remaining audit logs were produced with the installed `hygger-site-factory-flat/audits/` and its bundled `assets/source-skills/hugo-site-factory/` audit scripts. Browser audits require Playwright Chromium and its system libraries.
