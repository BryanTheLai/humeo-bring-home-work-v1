# Humeo

Long interview or podcast → vertical 9:16 shorts. FFmpeg render. Gemini for selection, hooks, pruning, layout. OpenAI or WhisperX for transcription.

## Two packages

| Path | Role |
|------|------|
| `src/humeo/` | Product CLI: ingest, LLM stages, cache, render orchestration. |
| `humeo-core/` | Shared schemas, primitives (`ingest`, `compile`, vision helpers), optional MCP server. |

## Requirements

- **Python** ≥ 3.10  
- **uv** (recommended) — install: [astral.sh/uv](https://docs.astral.sh/uv/)  
- **ffmpeg** on `PATH`  
- **API keys** — see `docs/ENVIRONMENT.md`: Gemini required (`GOOGLE_API_KEY` or `GEMINI_API_KEY`); OpenAI if you use Whisper API (`OPENAI_API_KEY` + `HUMEO_TRANSCRIBE_PROVIDER=openai`)

## Install

```bash
uv venv
uv sync
```

Optional local Whisper (GPU stack): `uv sync --extra whisper`

## Configure

Copy `.env.example` → `.env`. Never commit `.env`.

## Run

```bash
humeo --long-to-shorts "https://www.youtube.com/watch?v=VIDEO_ID"
```

Flags, cache dirs, models: `docs/ENVIRONMENT.md`. Stage-by-stage behavior: `docs/PIPELINE.md`.

## Pipeline (high level)

1. Ingest: download, extract audio, transcribe → `transcript.json`  
2. Clip selection (Gemini) → `clips.json`  
2.25. Hook detection (Gemini) → `hooks.json`  
2.5. Content pruning (Gemini) → `prune.json`  
3. Keyframes + layout vision (Gemini) → `layout_vision.json`  
4. Render (ffmpeg) → MP4s under `output/` (gitignored)

## Layout model

A short shows at most **two** on-screen items (`person` or `chart`). Five layouts:

| Layout | Items |
|--------|--------|
| `zoom_call_center` | 1 person |
| `sit_center` | 1 person |
| `split_chart_person` | 1 chart + 1 person |
| `split_two_persons` | 2 persons |
| `split_two_charts` | 2 charts |

Full terms: `TERMINOLOGY.md`.

## Documentation

| Doc | Content |
|-----|---------|
| `docs/STUDY_ORDER.md` | Reading order for onboarding. |
| `docs/PIPELINE.md` | Stages, caches, artifacts. |
| `docs/ENVIRONMENT.md` | Keys, env vars, CLI mapping. |
| `docs/SHARING.md` | Public repo, GitHub Pages, what is not in git. |
| `docs/TARGET_VIDEO_ANALYSIS.md` | Example target input / quality bar. |
| `docs/hive_architecture_visualization.html` | Static architecture diagram (HIVE-inspired). |
| `docs/full_run_output.txt` | Example full run log. |
| `docs/hive-paper/` | HIVE paper notes and prompts excerpt. |
| `TERMINOLOGY.md` | Glossary. |
| `humeo-core/docs/ARCHITECTURE.md` | Core engine layout. |

Backlog and future work: `docs/TODO.md`.

## Sharing demos

Large outputs (`output/`, `*.mp4`) are **not** committed. Put shorts on **YouTube** (or similar) and link them.

Host **`docs/hive_architecture_visualization.html`**: enable **GitHub Pages** from `/docs` — steps in `docs/SHARING.md`. Entry page: `docs/index.html`.

## Test

```bash
uv sync --extra dev
uv run pytest
```

## License

MIT — see `LICENSE`.

## Contributing

Issues and PRs welcome. Run `uv run pytest` before you push. Match existing style; keep changes focused.
