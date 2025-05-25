# Speed Demo Script for OpenAI TTS-1 Model
from pathlib import Path
from openai import OpenAI
import time

client = OpenAI()

speed_tests = [
    {"speed": 1.0, "text": "This is normal speed.", "filename": "speed_normal.mp3"},
    {"speed": 2.0, "text": "This is double speed.", "filename": "speed_double.mp3"},
    {"speed": 0.5, "text": "This is half speed.", "filename": "speed_half.mp3"},
]

def generate_speed_sample(speed, text, filename):
    speech_file_path = Path(__file__).parent / filename
    print(f"Generating: '{text}' (speed={speed}) -> {filename}")
    try:
        with client.audio.speech.with_streaming_response.create(
            model="tts-1",
            voice="alloy",
            input=text,
            response_format="mp3",
            speed=speed
        ) as response:
            response.stream_to_file(speech_file_path)
        print(f"✅ Success: {filename}")
    except Exception as e:
        print(f"❌ Error generating {filename}: {e}")

if __name__ == "__main__":
    print("\n=== TTS-1 Speed Demo ===\n")
    for test in speed_tests:
        generate_speed_sample(test["speed"], test["text"], test["filename"])
        time.sleep(0.5)
    print("\nDone! Listen to speed_normal.mp3, speed_double.mp3, and speed_half.mp3.")
