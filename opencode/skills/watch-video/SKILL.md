---
name: watch-video
description: Extract frames from a video file for visual analysis. Use when the user says 'watch this video', 'watch video', 'watch the video', 'analyze this video', 'extract frames', 'what happens in this video', 'summarize this video', or provides a .mp4, .mov, or .avi file path.
---

# Watch Video

Watch and understand a video by analyzing its frames and audio.

## Prerequisites

- `ffmpeg` installed:
  - macOS: `brew install ffmpeg`
  - Linux/WSL: `sudo apt install ffmpeg`
  - Windows: `choco install ffmpeg`
- `openai-whisper` installed (optional, for audio transcription) — `pip3 install openai-whisper`

## Steps

Ensure dependencies are installed:

```bash
ffmpeg -version >/dev/null 2>&1 || echo "Warning: ffmpeg not installed. Follow the Prerequisites to install it."
python3 -c "from PIL import Image" 2>/dev/null || pip3 install Pillow
```

1. Determine the video file path from the user's message or from a previous download step.
2. Extract frames using the `extract-frames.py` script bundled in this skill's `scripts/` directory:
   ```bash
   python3 scripts/extract-frames.py "<video-path>" "<output-dir>/.video-frames"
   ```
   This MUST be a single-line command. Never inline the extraction logic as a multi-line bash block — always call the script.
   Derive `<output-dir>` from the video file's parent directory (e.g. `~/Downloads/path/to/video.mp4` → `~/Downloads/path/to`). If the parent directory is not suitable, fall back to the system temp directory.
   The script automatically determines the frame interval based on video duration and outputs frame paths.
3. Transcribe audio using the `transcribe-audio.py` script:
   ```bash
   python3 scripts/transcribe-audio.py "<video-path>" "<output-dir>/.video-frames" [language]
   ```
   Use the same `<output-dir>` as step 2. The optional `language` argument (default: `en`) sets the Whisper language hint — use ISO 639-1 codes (e.g. `en`, `ja`, `ko`, `zh`). The script skips gracefully if the video has no audio stream, if the audio is mostly silence/noise, or if Whisper is not installed.
   If a transcript is produced, read it and incorporate the spoken content into your analysis.
4. Read the extracted frames as images and analyze them sequentially to understand what the video shows. If a transcript exists, cross-reference the visual content with the spoken content.

   **Batching:** The image read tool accepts at most 10 images per call. If the extraction produced more than 10 frames, read them in multiple batches of up to 10 (e.g. frames 1–10, then 11–20, etc.). Read ALL frames — never skip or sample. Analyze each batch before reading the next so you can track state transitions across the full video.
5. Provide a summary of the video content based on the frames and transcript.


