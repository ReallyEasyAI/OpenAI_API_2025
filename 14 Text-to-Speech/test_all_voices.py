# Test all available voices with different models
from pathlib import Path
from openai import OpenAI
import time

client = OpenAI()

# All supported voices according to documentation
VOICES = ["alloy", "ash", "ballad", "coral", "echo", "fable", "onyx", "nova", "sage", "shimmer", "verse"]

def test_voice(voice, model="tts-1"):
    """Test a specific voice with given model"""
    speech_file_path = Path(__file__).parent / f"voice_{voice}_{model.replace('-', '_')}.mp3"
    
    print(f"Testing voice '{voice}' with model '{model}'...")
    
    try:
        with client.audio.speech.with_streaming_response.create(
            model=model,
            voice=voice,
            input=f"Hello, I am the {voice} voice speaking with the {model} model. How do I sound?",
            response_format="mp3"
        ) as response:
            response.stream_to_file(speech_file_path)
        
        print(f"✅ Generated: {speech_file_path.name}")
        
    except Exception as e:
        print(f"❌ Error with voice '{voice}': {e}")

print("🎤 Testing All Available Voices 🎤")
print("=" * 40)

# Test a few voices with TTS-1 (fast generation)
print("\n--- Testing voices with TTS-1 model ---")
for voice in ["alloy", "nova", "coral", "echo", "shimmer"]:
    test_voice(voice, "tts-1")
    time.sleep(0.5)  # Small delay to avoid rate limiting

print("\n--- Testing with GPT-4o-Mini-TTS (with instructions) ---")
# Test one voice with instructions
speech_file_path = Path(__file__).parent / "voice_instructions_demo.mp3"

try:
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="ballad",
        input="This demonstrates the instruction feature of GPT-4o-Mini-TTS. Notice how the voice changes based on the instructions provided.",
        instructions="Speak in a dramatic, theatrical style with varied intonation and clear enunciation.",
        response_format="mp3"
    ) as response:
        response.stream_to_file(speech_file_path)
    
    print(f"✅ Instructions demo generated: {speech_file_path.name}")
    
except Exception as e:
    print(f"❌ Error with instructions demo: {e}")

print("\n🎉 Voice testing complete!")
print(f"Available voices: {', '.join(VOICES)}")
print("\nListen to the generated files to compare the different voices!")
