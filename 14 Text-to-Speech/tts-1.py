# TTS-1 Model - Basic quality, fastest generation
from pathlib import Path
from openai import OpenAI

client = OpenAI()
speech_file_path = Path(__file__).parent / "speech_tts1.mp3"

print("Generating speech with TTS-1 model (basic quality, fastest)...")

try:
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        input="This is generated using the TTS-1 model, which is optimized for speed and real-time applications.",
        response_format="mp3",
        speed=1  # Speed control works with tts-1
    ) as response:
        response.stream_to_file(speech_file_path)
    
    print(f"TTS-1 speech successfully generated: {speech_file_path}")
    
except Exception as e:
    print(f"Error with TTS-1 model: {e}")
