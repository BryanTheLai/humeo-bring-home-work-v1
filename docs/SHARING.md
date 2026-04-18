# Sharing this project with someone else

Large binaries do not belong in git. `.gitignore` excludes **`output/`**, **`*.mp4`**, **`*.wav`**, **`keyframes/`**. That is intentional.

## What lives in the repo

- Markdown in `docs/`
- `docs/hive_architecture_visualization.html` (static; can be served by GitHub Pages)
- `docs/full_run_output.txt` (example log; text is small enough to commit)

## Easiest ways to show work

1. **Public GitHub repo** — They browse code and docs on GitHub.
2. **GitHub Pages** — Host the architecture HTML without a separate server. Example (replace org/user if yours differs):
   - `https://<user>.github.io/<repo>/hive_architecture_visualization.html`
3. **Raw file links** — One-click read-only view of a tracked file:
   - `https://raw.githubusercontent.com/<user>/<repo>/<branch>/docs/full_run_output.txt`
   - Same pattern for `docs/TARGET_VIDEO_ANALYSIS.md` (Opens as plain text; for rendered Markdown use the GitHub blob URL.)
4. **YouTube** — Upload rendered shorts. Repo stays small; video is the demo.

## What you cannot share via git alone

- Final **`short_*.mp4`** files unless you remove ignore rules or use **GitHub Releases** / external storage.

Use YouTube or Releases for MP4s; keep git for source and documentation.
