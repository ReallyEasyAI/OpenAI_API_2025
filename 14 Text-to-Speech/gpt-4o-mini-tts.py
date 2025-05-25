# GPT-4o-Mini-TTS Model - Latest model with instruction support
from pathlib import Path
from openai import OpenAI

client = OpenAI()
speech_file_path = Path(__file__).parent / "speech_gpt4o_mini_tts.mp3"

print("Generating speech with GPT-4o-Mini-TTS model (supports instructions)...")

try:
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input="This is generated using the GPT-4o-Mini-TTS model, which supports custom voice instructions for more control.",
        instructions="Speak in a calm, professional tone with slight emphasis on technical terms.",
        response_format="mp3"
        # Note: speed parameter does NOT work with gpt-4o-mini-tts
    ) as response:
        response.stream_to_file(speech_file_path)
    
    print(f"GPT-4o-Mini-TTS speech successfully generated: {speech_file_path}")
    
except Exception as e:
    print(f"Error with GPT-4o-Mini-TTS model: {e}")
