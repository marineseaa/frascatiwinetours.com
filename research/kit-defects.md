# Scaffold corrections recorded during this build

The installed kit was not modified. These are candidate reusable fixes for a future kit update.

- Restrict the runtime `data-gyg-href` injector to anchors. Selecting widget divs as well can overwrite their provider URLs.
- Derive mobile-header prices and guide CTAs from the current page's featured product. A catalogue minimum or global featured product can send visitors to a different experience.
- Make comparison-table highlight data page-specific. A themed landing page must not inherit another product's price or booking destination.
- Keep homepage gallery data scoped to the homepage; tour pages should use their own galleries.
- Remove unsupported scaffold claims such as guest nationality totals and invented business contact details; only publish verified operator facts.
- Guard structured-data prices and aggregate review counts and preserve raw price precision. Visible amounts use one shared rounding formatter.
- Include section indexes in the homepage Explore inventory, alongside regular pages.
- Keep hook graphics below the opening guide sections so automatic booking widgets retain the intended placement.
- Use an explicit writable absolute Hugo cache path in restricted local environments.

The site uses a balanced three-column desktop row for its three detailed-tour cards. This small layout adaptation avoids a lone card while preserving the flat design system.
