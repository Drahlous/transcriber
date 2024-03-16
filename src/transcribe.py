import whisper
import sys
import os
from pathlib import Path

def transcribe(filepath):
    # Transcribe the audio
    model = whisper.load_model("small.en")
    result = model.transcribe(filepath, verbose=True)

    # Create a general output directory
    output = Path("output")
    output.mkdir(parents=True, exist_ok=True)

    # Create an output directory specifically for this result
    filename = str(os.path.basename(filepath)).split('.')[0]
    output = Path(output, filename)
    output.mkdir(parents=True, exist_ok=True)

    # Write output to a file
    output_writer = whisper.utils.get_writer("all", output)
    output_writer(result, filename)

if __name__ == "__main__":
    filename = sys.argv[1]

    print(filename)
    transcribe(filename)