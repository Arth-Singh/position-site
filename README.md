# Position site: a research exchange for AI safety

Static site for the position paper "AI Safety Needs a Research Exchange Between Frontier Labs and Academia
Alongside the Talent Pipeline". Served by GitHub Pages from the `main` branch.

## Files

- `index.html`: the whole page, styles inline. Fonts from Google Fonts (Newsreader, IBM Plex Mono).
- `assets/cover.jpg`: the Babel painting. `assets/access_by_tier.png`: Figure 2 from the paper.
- `signatories.json`, `views.json`: rendered by the page's script. Written by the workflow below.
- `.github/ISSUE_TEMPLATE/sign.yml`: the sign form. Opening it creates an issue labeled `signature`.
- `.github/ISSUE_TEMPLATE/alternative-view.yml`: the view form. Creates an issue labeled `alternative-view`.
- `.github/workflows/signatories.yml` and `scripts/add_entry.py`: on a `signature` issue, append the entry
  to `signatories.json`, thank the signer and close the issue. On an `alternative-view` issue, nothing happens
  until a maintainer adds the `accepted` label; then the view is appended to `views.json`.

## Moderation

Signatures are added without review; remove one by deleting its row from `signatories.json`. Views are added
only when labeled `accepted`. Spam issues can be closed and deleted as usual.

## To do

- Replace `[GOOGLE FORM URL]` in `index.html` with a form for people without a GitHub account, and merge its
  responses into `signatories.json` by hand or with a second workflow.
- Numbers on the page come from the paper's generated macros as of 20 September 2026. Update them together with
  the paper.
