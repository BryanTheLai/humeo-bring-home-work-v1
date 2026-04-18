# Sharing this project

## What never ships in git (by design)

- `.env` — secrets.
- `output/`, `*.mp4`, `*.wav` — large renders and downloads.
- Local work dirs — `.humeo_work*`, `.humeo_work_clean*` (see `.gitignore`).

Demo videos: use **YouTube** (or another host). Link the playlist or single video in PRs and README.

## What does ship in git

- `docs/hive_architecture_visualization.html` — static architecture page.
- `docs/full_run_output.txt` — example pipeline log.
- `docs/TARGET_VIDEO_ANALYSIS.md` — input / test-case notes.
- `README.md` and `docs/*.md` — how to run and what each stage does.

## Easiest ways for someone to open files

### A) Public GitHub repo (no hosting setup)

Use **raw** or **blob** URLs:

- `https://github.com/<OWNER>/<REPO>/blob/main/docs/hive_architecture_visualization.html` — browser shows HTML source unless you use raw.
- `https://raw.githubusercontent.com/<OWNER>/<REPO>/main/docs/hive_architecture_visualization.html` — raw only; not a full page UX.

For **rendered HTML**, use GitHub Pages (B) or paste the HTML into any static host.

### B) GitHub Pages (simplest rendered HTML)

1. Repo **Settings → Pages**.
2. **Build and deployment**: source **Deploy from a branch**.
3. Branch **main**, folder **`/docs`**, Save.
4. Site base: `https://<OWNER>.github.io/<REPO>/`
5. Open: `https://<OWNER>.github.io/<REPO>/hive_architecture_visualization.html`  
   Or open `docs/index.html` at `https://<OWNER>.github.io/<REPO>/` (links hub).

No paid tiers required for public repos on standard GitHub.

### C) Other static hosts

Drop `docs/hive_architecture_visualization.html` on Netlify, Cloudflare Pages, or any host that serves static files. Same file; no build step.
