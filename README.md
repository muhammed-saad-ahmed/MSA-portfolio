# Muhammad Saad Ahmed: Portfolio

A premium, single-page personal portfolio built with Python and Streamlit. It uses a custom
design system (Midnight Executive dark theme plus a light theme), scroll-triggered reveals,
and a fixed translucent navigation bar. No API keys, database or paid services are needed.

## Project structure

```
msa-portfolio/
├── app.py                  # Entry point: assembles the page
├── requirements.txt
├── .streamlit/config.toml  # Theme + hides Streamlit chrome
├── assets/
│   └── portrait.jpg        # YOUR PHOTO (already included, replace to change)
├── styles/main.css         # Complete stylesheet
└── components/
    ├── data.py             # ALL text content: edit this to change the site
    ├── sections.py         # HTML for each section
    └── utils.py            # Image loading, themes, helpers
```

## Run locally (VS Code)

1. Install Python 3.10+ from python.org (tick "Add to PATH").
2. Unzip the project and open the `msa-portfolio` folder in VS Code (File → Open Folder).
3. Open the terminal in VS Code (Ctrl + `) and run:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

The site opens at http://localhost:8501.

## Your photograph

The portrait is loaded from `assets/portrait.jpg`. Replace that file with another photo
(same filename, JPG, ideally under 500 KB) to change it. If the file is missing the site still
works and shows an "MSA" placeholder.

## Editing content

Open `components/data.py`. Each section has a clearly named block:

- `EXPERIENCE`: add verified dates and responsibilities for UXGENIE (currently empty on purpose).
- `CERTIFICATIONS`: add real certificates, for example
  `{"title": "Snowflake Hands-On Essentials", "issuer": "Snowflake", "year": "2025"}`.
  The Certifications block appears automatically once the list has items.
- `MORE_WORK`: when Mini Data Warehouse, your cloud work or Savoraise get public repositories,
  change `"repo": None` to the repository URL and a button appears.
- Theme link: visitors can switch themes with the Light/Dark button; `?theme=light` also works in the URL.

## Publish to GitHub

1. Create a new **public** repository on github.com (for example `portfolio`). Leave it empty.
2. In the project folder:

```bash
git init
git add .
git commit -m "Initial portfolio"
git branch -M main
git remote add origin https://github.com/muhammed-saad-ahmed/portfolio.git
git push -u origin main
```

## Deploy on Streamlit Community Cloud (free)

1. Go to https://share.streamlit.io and sign in with GitHub.
2. Click **Create app** → **Deploy a public app from GitHub**.
3. Repository: `muhammed-saad-ahmed/portfolio`, Branch: `main`, Main file path: `app.py`.
4. Click **Deploy**. After a minute you get a public `*.streamlit.app` URL that anyone can open
   without logging in. In Advanced settings you can choose a custom subdomain.

## Troubleshooting

- **`streamlit` is not recognised**: activate the virtual environment, or run `python -m streamlit run app.py`.
- **Layout looks unstyled**: hard refresh (Ctrl+Shift+R). The page needs internet access for Google Fonts; it falls back to system fonts otherwise.
- **Photo missing**: confirm the file is exactly `assets/portrait.jpg` and committed to Git.
- **Navigation links do not scroll**: use a current Streamlit version (`pip install -U streamlit`). Clicking Home/About etc. uses in-page anchors.
- **Animations not showing**: scroll reveals use CSS scroll-driven animation, supported in recent Chrome and Edge. Other browsers show the content without the reveal effect, which is intended.
- **Streamlit Cloud shows "Oh no" error**: open "Manage app" → logs, and check that `requirements.txt` is in the repository root.

## Known limitations of Streamlit

Streamlit does not allow custom JavaScript inside the page, so this site is pure HTML/CSS.
That means the navigation bar does not highlight the active section while scrolling (hover
states are provided instead), and the theme switch reloads the page.


## Portfolio V2 updates (October 2026)

- Official KRYPTA and Tadabbur AI logo artwork embedded in the corresponding project case studies.
- Hero portrait now preserves the original image aspect ratio without cutting off the subject.
- Adamjee HSC Pre-Engineering marked completed (2026) throughout the public content.
- Original application architecture, section sequence, and file locations retained.
- Optimized WebP logo assets are stored in `assets/`.


## Portfolio V2.1 updates (November 2026)

- Consolidated project case studies from both supplied GitHub profiles and the accessible LinkedIn activity.
- Added Mini Data Warehouse, Real-Time Weather Data Pipeline, and Weather Forecast Dashboard. KRYPTA remains the sole Karachi infrastructure-risk project; the earlier Karachi-infrastructure-intelligence repository is intentionally excluded.
- Added repository and live-demo links where they were present in the public LinkedIn project posts.
- Added a grouped section for additional Saylani coursework repositories.
- Added Fiverr and the second GitHub profile to the portfolio's external profile links.
- Updated the UXGENIE internship period and verified experience summary from the LinkedIn post.
- Fiverr portfolio project details still need to be added after the profile's project entries are supplied or become publicly accessible.


## Portfolio content note

- The earlier `Karachi-infrastructure-intelligence` / Karachi Pulse project is intentionally not listed; KRYPTA is the current project for that work.
- The hero-name gradient uses theme-aware colours so “Ahmed” remains readable in light mode.

- The KRYPTA WebP logo is bundled in `assets/krypta-logo.webp` and is displayed in the flagship project panel.
- Fiverr's portfolio gallery did not expose its individual project entries to public retrieval during this update. The Fiverr profile link is included, but individual Fiverr case studies and thumbnails must be added from screenshots or exported project details supplied by the account owner.
