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


Hmm make ths cli?
```zsh
humeo --long-to-shorts "{youtube_link}"
```

Like simple right.

Then this video i am aiing to edit.
It has basically 3 main positions for the subject.
1 .zoom call in the midle of the scrreen zoomed in more compared to 3.
2. 1 chart leftside that taaeks up 2/3, 1 human right side that takes 1/3
3. human right middle but zoomed out more compared to 1.

Ok so now 2 options.
1. for this video just manually set the subjects for the video somehow. 
- ui to drag and highlight subject? 
- model that detects subject?
i dk how to design, build both, what models to use, how to create subject selector ui?

2. just use 4:3 put it in the 9:16 video. so its in the middle, top and bottom will have black bard, fill the top with title. Bottom with nothing.

3. 1 subject focus only. but still need:
- ui to drag and highlight subject? 
- model that detects subject?
i dk how to design, build both, what models to use, how to create subject selector ui?

Hmm so maybe im missing something, u could help me with thnking about this.