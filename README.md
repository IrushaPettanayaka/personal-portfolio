# Irusha Pettanayaka — personal portfolio

A Flask portfolio focused on mathematics, programming, AI, and data engineering. The homepage uses an editorial framed hero built around “Drawn to mathematics. Learning through code.”, followed by a concise About section, a restrained project invitation, and a direct LinkedIn contact path. The separate archive contains ten explicit project entries, grouped into selected work and smaller practice/course exercises, with optional category filters.

## Development and attribution

I developed the portfolio’s HTML structure and its initial, smaller CSS styling. I used OpenAI Codex for the larger improvements, including the refined visual system, responsive layout, accessibility work, interactions, testing, and deployment preparation.

## Run in VS Code on Windows

Open this folder in VS Code, then **Terminal → New Terminal** (PowerShell).

First-time setup:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Start the site:

```powershell
.\.venv\Scripts\python.exe -m flask --app app run --debug
```

Open [Homepage](http://127.0.0.1:5000/) or [Projects](http://127.0.0.1:5000/projects). Stop with `Ctrl+C`. If port 5000 is occupied, append `--port 5002` and open that port. Virtual-environment activation is unnecessary. Use Flask rather than Live Server; Jinja templates need Python rendering.

Python 3.10+ is required. Checks used Python 3.14 and Flask 3.1.2. No frontend framework, build pipeline, database, or visitor-time GitHub request is used. Nothing has been deployed.

## Deploy on Render

Create a Python Web Service from this repository with:

```text
Build command: pip install -r requirements.txt
Start command: gunicorn app:app
Health check path: /
```

The checked-in site requires no database or environment variables.

## Editing

- `content.py`: profile copy, education, current focus, navigation, filter labels, and an explicit dictionary for every project. Maintain exact case-sensitive GitHub paths. Missing email remains `None` and renders no email link.
- `templates/index.html`: editorial homepage composition with the framed hero and concise supporting sections.
- `templates/projects.html`: server-rendered complete project index, descriptive project links, unique page metadata, and native filter buttons.
- `static/js/projects.js`: progressive enhancement for the filters only. Each project's `filter` key matches a key in `FILTERS`; category text can be edited independently. All entries show initially and after refresh. JavaScript updates project and empty-group visibility, `aria-pressed`, and the live project count. The controls remain hidden until initialized, so a script failure leaves the complete archive visible.
- `static/js/theme.js`: accessible dark/light theme control with guarded local persistence. The small inline script in `base.html` applies a saved choice before the stylesheet paints.
- `static/css/style.css`: shared dark/light tokens, framed surface treatment, serif headline accent, responsive project rows, visible focus states, and reduced-motion rules.
- `app.py`: routes. The old Task Tracker detail URL redirects to `/projects#task-tracker`.
- `templates/base.html` and `templates/404.html`: shared shell and missing-page response.
- `tests/test_app.py`: eleven route, asset, content, inventory, metadata, theme, and fallback checks.

Keep Jinja autoescaping. The maths widget and its calculation code remain removed. Original screenshots and video are preserved locally but are not shown in the archive. Manrope is served locally as WOFF2 with its license in `static/fonts/OFL.txt`. The 1200 × 630 social preview is `static/images/social-preview.png`.

## Verified inventory and sources

The account's public repository listing and recursive trees were rechecked on 7 October 2026. The four owned repositories and the supplied Aegis team repository were inspected. The small-project trees were not truncated and contained no additional standalone projects beyond those below. Implementation files inside Gesture Defender and Aegis were not treated as separate products.

| Project | Repository / inspected source |
| --- | --- |
| Task Tracker | `Python_mini_projects`: `task_tracker/task_tracker.py` |
| Number Guesser | `Python_mini_projects`: `number_guesser.py` |
| Number Guessing: Early Version | `Python_mini_projects`: `Number_guessing.py` |
| Rock–Paper–Scissors | `Python_mini_projects`: `Rock_paper_scissors.py` |
| Dice Roller | `Python_mini_projects`: `game.py` |
| Caesar Cipher | `FreeCodeCamp_projects_python`: `caesar_cipher/main.py` |
| PIN Extractor | `FreeCodeCamp_projects_python`: `pin_extractor/main.py` |
| Python Calculator | `PythonProject_Irusha_Pettanayaka`: `Python_calculator/calculator.py` |
| Aegis Engine | `aasim10-Volt/aegis`: README, `package.json`, `aegis/engine/phase_b_teams.py`, `aegis/engine/phase_c_health.py` |
| Gesture Defender | `gesture-defender`: README, `requirements.txt`, `hand_tracking.py` |

All eight small Python source files were read in full. Source links in `content.py` point directly to those files. The application entries link to their repositories. Aegis's readme, package dependencies, and team-formation/health source support its short description and technologies. Gesture Defender's readme explicitly discloses substantial Codex assistance; its card uses the user's requested contribution statement. Repository ownership is not presented as proof of independent authorship.

Repositories:

- [Python mini projects](https://github.com/IrushaPettanayaka/Python_mini_projects)
- [freeCodeCamp Python projects](https://github.com/IrushaPettanayaka/FreeCodeCamp_projects_python)
- [Python calculator repository](https://github.com/IrushaPettanayaka/PythonProject_Irusha_Pettanayaka)
- [Aegis team repository](https://github.com/aasim10-Volt/aegis)
- [Gesture Defender](https://github.com/IrushaPettanayaka/gesture-defender)

`ZAID-EHT/Aegis-backend` returned 404 from both the public GitHub API and the connected GitHub file read. Its contents and relationship to Aegis could not be verified. No backend link or second product was invented. An accessible repository URL or appropriate connected access is needed before adding that source link.

## Verification performed

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

- **Eleven tests passed**: homepage/Projects routes and links, referenced assets, all ten explicit entries, grouped project order, descriptive source links, metadata and social preview, WOFF2 font integrity, category counts, team/AI attribution, theme assets/tokens, optional email, escaping, removed widget, redirect, and 404 behavior.
- Browser checks of homepage and Projects at **360px**, **390px**, and desktop. No horizontal overflow; navigation, headline, and project rows adapt cleanly on mobile.
- Verified the dark and light themes on both pages, keyboard-operated the theme control, navigated between pages, and reloaded to confirm persistence.
- Operated filters using Tab, Enter, and Space. Counts were All 10, Python practice 6, Course exercises 2, Team projects 1, AI-assisted 1. Both guessing versions remain separate. Refresh returns to All.
- Verified the muted-blue keyboard focus outline on the theme control and filters.
- Tested `/projects` in a separate local preview with `Content-Security-Policy: script-src 'none'`: the dark theme loaded, all ten entries remained visible, and both theme/filter controls stayed hidden.
- Normal-preview console logs contained no errors or warnings.
- Calculated text contrast for the main, secondary, accent, and button text pairs against page/surface backgrounds in both themes: minimum **5.55:1**. This is a palette check, not a full accessibility certification.
- Inspected browser-loaded reduced-motion CSS: smooth scrolling is disabled and transitions/animations are removed. Native OS reduced-motion emulation was unavailable, so that preference was not directly exercised. Other browser engines, screen readers, and native zoom were not tested.

Screenshots are under `verification/`, outside served assets. No deployment was performed.
