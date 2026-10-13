# Frascati Wine Tours

Local Hugo travel affiliate website for frascatiwinetours.com. Built with Marina's flat design: Cormorant Garamond headings, Source Sans 3 body text, burgundy buttons, warm ivory backgrounds and olive accents. Both fonts are self-hosted; their licenses ship in `static/fonts/`.

## Build and preview

Requires Hugo extended 0.146 or newer. This build was verified with 0.164.

```bash
./scripts/build.sh
python3 scripts/verify-site.py
python3 -m http.server 1313 --directory public
```

Open http://localhost:1313. The production output is in `public/`; it is deliberately excluded from Git and recreated by the build command. The build script places Hugo's cache in the system temporary directory. Preview the production directory directly to preserve its canonical URLs.

## Content and booking

The site contains a homepage, three detailed tours, two themed landing pages, four guides, two section indexes, two legal pages and a 404 page: 15 HTML documents altogether. The homepage Explore section links to every content destination. Tour galleries use distinct real listing photographs; the four guides include explanatory graphics.

Catalogue data lives in `data/gyg_frascati_offers.json`; editorial pages are in `content/`. Sources, review provenance, expected page inventory and captured evidence live in `research/`. Product details were checked on 13 October 2026. Prices, review totals and operator arrangements are dated snapshots; refresh the catalogue before subsequent publication when necessary. Review cards are labelled paraphrases, not verbatim quotations.

Partner ID **1MSALBX** comes from the supplied project analytics snippet. Campaign **frascatiwinetours** is consistent across the configuration, widgets and runtime booking links. When changing these, update `hugo.toml` and `static/js/main.js` together and run the verifier. Every affiliate CTA has a direct product URL fallback if JavaScript is unavailable.

Three homepage cards link to complete tour pages. The lower-priced Roman wine-cave cooking class appears only as a contextual alternative; it is not presented as a vineyard excursion. Train tickets are explicitly excluded from the train-based featured experiences.

## Validation and delivery

See [QA-REPORT.md](QA-REPORT.md) for results and `research/qa/` for audit logs and desktop, tablet and mobile screenshots. This is a local build, with a local Git repository on `master` and no remote. It has not been deployed. Hosting redirects, production response headers and live-domain behavior require verification after deployment.
