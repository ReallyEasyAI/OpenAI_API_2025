# TTS-1-HD Model - Higher quality, slower generation
from pathlib import Path
from openai import OpenAI

client = OpenAI()
speech_file_path = Path(__file__).parent / "speech_tts1_hd.mp3"

print("Generating speech with TTS-1-HD model (higher quality)...")

try:
    with client.audio.speech.with_streaming_response.create(
        model="tts-1-hd",
        voice="alloy",
        input="This is generated using the TTS-1-HD model, which provides higher quality audio with increased latency.",
        response_format="mp3",
        speed=1  # Speed control works with tts-1-hd
    ) as response:
        response.stream_to_file(speech_file_path)
    
    print(f"TTS-1-HD speech successfully generated: {speech_file_path}")
    
except Exception as e:
    print(f"Error with TTS-1-HD model: {e}")
