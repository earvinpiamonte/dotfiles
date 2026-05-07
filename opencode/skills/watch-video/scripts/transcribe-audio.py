#!/usr/bin/env python3
import json
import os
import subprocess
import sys
import tempfile

video = sys.argv[1] if len(sys.argv) > 1 else ""

output_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(tempfile.gettempdir(), "video-frames")

language = sys.argv[3] if len(sys.argv) > 3 else None

if not video or not os.path.isfile(video):
    print(f"Error: Video file not found: {video}", file=sys.stderr)
    sys.exit(1)

# Check if video has an audio stream
probe = subprocess.run(
    ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_streams", "-select_streams", "a", video],
    capture_output=True, text=True
)

try:
    streams = json.loads(probe.stdout).get("streams", [])
except json.JSONDecodeError:
    streams = []

if not streams:
    print("No audio stream found. Skipping transcription.")
    sys.exit(0)

basename = os.path.splitext(os.path.basename(video))[0]

frame_dir = os.path.join(output_dir, basename)

os.makedirs(frame_dir, exist_ok=True)

audio_path = os.path.join(frame_dir, "audio.wav")

# Extract audio as 16kHz mono WAV
subprocess.run(
    ["ffmpeg", "-i", video, "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", audio_path, "-y"],
    capture_output=True
)

if not os.path.isfile(audio_path):
    print("Error: Failed to extract audio.", file=sys.stderr)
    sys.exit(1)


def is_silent(wav_path, threshold=500, min_speech_ratio=0.02):
    try:
        with open(wav_path, "rb") as f:
            f.read(44)

            data = f.read()

        if len(data) < 2:
            return True

        import array

        samples = array.array("h", data)

        loud_count = sum(1 for s in samples if abs(s) > threshold)

        return (loud_count / len(samples)) < min_speech_ratio
    except Exception:
        return False


if is_silent(audio_path):
    print("Audio is mostly silence/noise. Skipping transcription.")
    os.remove(audio_path)
    sys.exit(0)

# Transcribe using Whisper
try:
    import whisper  # type: ignore
except ImportError:
    print("openai-whisper not installed. Skipping transcription.")
    os.remove(audio_path)
    sys.exit(0)

model = whisper.load_model("base")

if language:
    result = model.transcribe(audio_path, language=language)
else:
    result = model.transcribe(audio_path)

transcript_path = os.path.join(frame_dir, "transcript.txt")

with open(transcript_path, "w") as f:
    f.write(result["text"].strip())

os.remove(audio_path)

print(f"Transcript saved to {transcript_path}")

print(result["text"].strip())
