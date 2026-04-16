Goal: Create engaging highlights of videos.

Input: Youtube video

Process:
1. Extract transcripts with timestamp
2. find the highlights in the video i can make short form videos out of, return in json format. JSON with time stamp and tarnscropts.
```json
--example
{
  "short_form_highlights": [
    {
      "id": 1,
      "topic": "The $5 Trillion Prediction Market Explosion",
      "start_timestamp": "4:49",
      "end_timestamp": "5:31",
      "viral_hook": "Prediction markets could explode to $5 trillion.",
      "transcript": "Um,.......... "
    },
    {
      "id": 2,
      "topic": "Prediction Markets vs. Traditional Derivatives",
      "start_timestamp": "3:44",
      "end_timestamp": "4:24",
      "viral_hook": "Prediction markets are the purest form of financial risk.",
      "transcript": "Yeah,......"
    }
  ]
}
```
design and improve this json to have more useful information.

3. Cut the video:
Use ffmpeg, cut these timelines out.
So into 2 videos in this case.

4. Horizontal to vertical:
<!-- Bcs we cant just rotate the video, identify all the important subjects.
<!-- Now detect the faces, and place them in shorts vertical format.
Exmaple, podcast, left and right.
Zoom into subject with approprate distance.
Then 1 top, 1 bottom. --> -->
Hmmm actually fuck it, just make it like this: https://www.youtube.com/shorts/dKAkONsYGDY
zoom out. Add title in video, then add subtitles. Done

5. Add transcripts in the middle.

Output: 2 short videos.