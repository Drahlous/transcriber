# Bulk Transcriber
 Bulk Transcription experiment powered by OpenAI Whisper

## Setup

Install OpenAI's Whisper Python Package:

```bash
pip install -U openai-whisper
```

Install `ffmpeg`:

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg
```

## Usage

Run the powershell script `run.ps1` with the path to the directory containing your video/audio files:

```ps1
.\run.ps1 data\test_audio
```