---
title: Podcast-to-Shorts Pipeline
type: mvp-spec
status: draft
---

# Podcast to shorts (product blurb)

**Goal:** Turn a long YouTube podcast or interview into several **9:16** MP4 shorts with burned subtitles and a title overlay.

**CLI:** `humeo --long-to-shorts "<youtube_url>"` (see repo root `README.md` for install and flags).

**How it works (one sentence):** Download + transcript → Gemini clip JSON → hook detection → inner-clip pruning → per-clip keyframe + layout vision → ffmpeg render.

**Canonical detail (do not duplicate here):** [`docs/PIPELINE.md`](PIPELINE.md) — stages, durations, caches, artifacts.

**Terminology:** [`TERMINOLOGY.md`](../TERMINOLOGY.md) — time window vs crop/layout.

**Gaps / roadmap:** [`docs/TODO.md`](TODO.md) (e.g. `narrative_context.json`, letterboxing). Prompt-vs-code quirks: [`docs/KNOWN_LIMITATIONS_AND_PROMPT_CONTRACT_GAP.md`](KNOWN_LIMITATIONS_AND_PROMPT_CONTRACT_GAP.md).

**Layout subject (zoom vs split chart):** Product uses Gemini vision + `humeo-core` layouts; open product questions live in `TODO.md` §3 (bbox / `split_fit`) rather than in this file.
