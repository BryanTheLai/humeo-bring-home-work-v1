---
title: Podcast-to-Shorts Pipeline
type: mvp-spec
status: draft
goal: Automate extraction of viral short-form videos from long-form YouTube podcasts.
input:
  - YouTube video URL
output:
  - Structured clip JSON
  - 9:16 MP4 shorts
---

# Podcast-to-Shorts Pipeline

## Goal
Automate extraction of viral short-form videos from long-form YouTube podcasts.

## Input
- YouTube video URL

## Process

### 1. Ingestion and transcription
- Download the source video.
- Generate a word-level transcript with exact timestamps.

### 2. Clip selection
- Analyze the transcript for strong 30-60 second segments.
- Return structured JSON for the editor.

```json
{
  "clips": [
    {
      "clip_id": "001",
      "topic": "Prediction Market Explosion",
      "start_time_sec": 289.0,
      "end_time_sec": 331.5,
      "duration_sec": 42.5,
      "viral_hook": "Prediction markets could explode to $5 trillion.",
      "virality_score": 0.94,
      "transcript": "Full text for subtitle generation...",
      "suggested_overlay_title": "$5T Prediction Markets"
    }
  ]
}
```

### 3. Segment cutting
- Parse the JSON.
- Use FFmpeg to cut each clip by `start_time_sec` and `end_time_sec`.

### 4. Vertical formatting
- Convert 16:9 into 9:16.
- Use a zoomed-out layout.
- Add a title at the top.
- Burn subtitles in the center.

## Output
- `N` short-form MP4 files.
- Ready for TikTok, YouTube Shorts, and Instagram Reels.