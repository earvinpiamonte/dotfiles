---
name: watch-video
description: Extract frames from a video file for visual analysis. Use when the user says 'watch this video', 'watch video', 'watch the video', 'analyze this video', 'extract frames', 'what happens in this video', 'summarize this video', 'listen to this video', 'listen', or provides a .mp4, .mov, or .avi file path.
---

# Watch Video

Watch and understand a video by analyzing its frames and audio.

## Prerequisites

- `ffmpeg` installed:
  - macOS: `brew install ffmpeg`
  - Linux/WSL: `sudo apt install ffmpeg`
  - Windows: `choco install ffmpeg`
- `Pillow` installed — `pip3 install Pillow` (on externally-managed environments, use `pip3 install --break-system-packages Pillow`)
- `openai-whisper` installed — `pip3 install openai-whisper` (required when the user asks to "listen" or transcribe audio; otherwise optional)

## Steps

Ensure dependencies are installed:

```bash
ffmpeg -version >/dev/null 2>&1 || echo "Warning: ffmpeg not installed. Follow the Prerequisites to install it."
python3 -c "from PIL import Image" 2>/dev/null || pip3 install Pillow 2>/dev/null || pip3 install --break-system-packages Pillow
```

1. Determine the video file path from the user's message or from a previous download step.
2. Extract frames using the `extract-frames.py` script bundled in this skill's `scripts/` directory:
   ```bash
   python3 scripts/extract-frames.py "<video-path>" "<output-dir>/.video-frames"
   ```
   This MUST be a single-line command. Never inline the extraction logic as a multi-line bash block — always call the script.
   Derive `<output-dir>` from the video file's parent directory (e.g. `~/Downloads/path/to/video.mp4` → `~/Downloads/path/to`). If the parent directory is not suitable, fall back to the system temp directory.
   The script automatically determines the frame interval based on video duration and outputs frame paths.
3. Check if the user explicitly asked to **listen** or transcribe the audio (e.g. prompt contains "listen", "listen to this", "what do they say", "transcribe"). If so, ensure `openai-whisper` is installed before proceeding:
   ```bash
   python3 -c "import whisper" 2>/dev/null || pip3 install openai-whisper 2>/dev/null || pip3 install --break-system-packages openai-whisper
   ```
4. Transcribe audio using the `transcribe-audio.py` script:
   ```bash
   python3 scripts/transcribe-audio.py "<video-path>" "<output-dir>/.video-frames"
   ```
   Only add a language code at the end if the user explicitly states the language or the visual context makes it obvious (e.g. a Japanese news broadcast → append `ja`).
   Use the same `<output-dir>` as step 2. The optional `language` argument lets you hint the audio language to Whisper (ISO 639-1 codes, e.g. `en`, `ja`, `ko`, `zh`, `tl`). **If you do not know the language, omit this argument** so Whisper auto-detects it.
   - If the user explicitly asked to listen/transcribe, do **not** skip transcription. Install `openai-whisper` first if it is missing.
   - If the user did not ask for audio analysis, the script may skip gracefully when the video has no audio stream, when the audio is mostly silence/noise, or when Whisper is not installed.
   If a transcript is produced, read it and incorporate the spoken content into your analysis.
5. Read the extracted frames as images and analyze them sequentially to understand what the video shows. If a transcript exists, cross-reference the visual content with the spoken content.

   **Batching:** The image read tool accepts at most 10 images per call. If the extraction produced more than 10 frames, read them in multiple batches of up to 10 (e.g. frames 1–10, then 11–20, etc.). Read ALL frames — never skip or sample. Analyze each batch before reading the next so you can track state transitions across the full video.
6. Provide a summary of the video content based on the frames and transcript.


