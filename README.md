# Humeo

Long podcast or interview → vertical 9:16 shorts. Pipeline: download, transcribe, Gemini (clip selection, hook detection, content pruning, layout vision), ffmpeg render.

**Architecture (static HTML, GitHub Pages):**  
[https://bryanthelai.github.io/humeo-bring-home-work-v1/hive_architecture_visualization.html](https://bryanthelai.github.io/humeo-bring-home-work-v1/hive_architecture_visualization.html)

## Repo layout

| Path | Role |
|------|------|
| `src/humeo/` | CLI, pipeline, ingest, Gemini prompts, render adapters |
| `humeo-core/` | Schemas, ffmpeg compile, primitives, optional MCP server |

## Pipeline (actual order)

```text
YouTube URL
  → ingest (source.mp4, transcript.json)
  → clip selection (Gemini → clips.json)
  → hook detection (Gemini → hooks.json)
  → content pruning (Gemini → prune.json)
  → keyframes + layout vision (Gemini vision → layout_vision.json)
  → ASS subtitles + humeo-core ffmpeg render → short_<id>.mp4
```

Details: **`docs/PIPELINE.md`**.

## Five layouts

A short shows at most two on-screen items (`person` or `chart`). That yields five layout modes (see **`TERMINOLOGY.md`**).

## Requirements

- **Python** ≥ 3.10  
- **`uv`** — install: [astral.sh/uv](https://docs.astral.sh/uv/)  
- **`ffmpeg`** — on `PATH` for extract/render  
- **API keys** — see **`docs/ENVIRONMENT.md`**  
  - `GOOGLE_API_KEY` or `GEMINI_API_KEY` — required for Gemini stages  
  - `OPENAI_API_KEY` — if using OpenAI Whisper API (`HUMEO_TRANSCRIBE_PROVIDER=openai`)

Copy **`.env.example`** → **`.env`** (never commit `.env`).

## Install

```bash
uv venv
uv sync
```

Optional local WhisperX (heavy; Windows often uses OpenAI API instead):

```bash
uv sync --extra whisper
```

## Run

```bash
humeo --long-to-shorts "https://www.youtube.com/watch?v=VIDEO_ID"
```

Use **`--work-dir`** or **`--no-video-cache`** to control where `source.mp4` and intermediates live (see **`docs/ENVIRONMENT.md`**).

## Documentation

| Doc | Purpose |
|-----|---------|
| **`docs/STUDY_ORDER.md`** | Read order for onboarding |
| **`docs/PIPELINE.md`** | Stages, caches, JSON contracts |
| **`docs/ENVIRONMENT.md`** | Keys, env vars, cache layout |
| **`docs/SHARING.md`** | How to share logs/docs/video without bloating git |
| **`docs/TARGET_VIDEO_ANALYSIS.md`** | Reference input analysis example |
| **`docs/full_run_output.txt`** | Example full run log (text) |
| **`docs/hive-paper/PAPER_BREAKDOWN.md`** | HIVE paper, file mapping §9 |
| **`docs/hive-paper/hive_paper_blunt_guide.md`** | Short HIVE recap |
| **`docs/TODO.md`** | Backlog |
| **`docs/SOLUTIONS.md`** | Design rationale |
| **`TERMINOLOGY.md`** | Glossary |

## Tests

```bash
uv sync --extra dev
uv run pytest
```

## Sharing outputs

`output/`, `*.mp4`, and `keyframes/` are **gitignored**. Put rendered shorts on **YouTube** or **GitHub Releases**; keep the repo for source and docs. See **`docs/SHARING.md`**.

## License

See **`LICENSE`** (root) and **`humeo-core/LICENSE`**.
