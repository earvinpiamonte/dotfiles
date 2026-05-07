#!/usr/bin/env python3
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile

from PIL import Image

video = sys.argv[1] if len(sys.argv) > 1 else ""

output_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(tempfile.gettempdir(), "video-frames")

if not video or not os.path.isfile(video):
    print(f"Error: Video file not found: {video}", file=sys.stderr)
    sys.exit(1)

basename = os.path.splitext(os.path.basename(video))[0]

frame_dir = os.path.join(output_dir, basename)

if os.path.exists(frame_dir):
    shutil.rmtree(frame_dir)

os.makedirs(frame_dir, exist_ok=True)

probe = subprocess.run(
    ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", video],
    capture_output=True, text=True
)

try:
    duration = float(json.loads(probe.stdout)["format"]["duration"])
except (json.JSONDecodeError, KeyError):
    print(f"Error: Could not read video duration. ffprobe output: {probe.stderr or probe.stdout}", file=sys.stderr)
    sys.exit(1)

if duration <= 300:
    interval = 2
else:
    interval = 4

max_frames = int(duration / interval)

subprocess.run(
    ["ffmpeg", "-i", video, "-vf", f"fps=1/{interval}", "-frames:v", str(max_frames), "-q:v", "2", os.path.join(frame_dir, "frame_%03d.jpg"), "-y"],
    capture_output=True
)

frames = sorted(glob.glob(os.path.join(frame_dir, "frame_*.jpg")))

MAX_DIM = 2000

for f in frames:
    img = Image.open(f)

    w, h = img.size

    if max(w, h) > MAX_DIM:
        scale = MAX_DIM / max(w, h)

        img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)

        img.save(f, "JPEG", quality=85)

print(f"Extracted {len(frames)} frames to {frame_dir}")

print(f"Duration: {duration}s | Interval: {interval}s | Max: {max_frames}")

for f in frames:
    print(f)
