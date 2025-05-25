# Compare all three TTS models
from pathlib import Path
from openai import OpenAI
import time

client = OpenAI()

def test_tts_model(model_name, voice, filename, use_instructions=False, use_speed=True):
    """Test a specific TTS model and measure generation time"""
    speech_file_path = Path(__file__).parent / filename
    
    print(f"\n--- Testing {model_name} ---")
    print(f"Voice: {voice}")
    print(f"Output: {filename}")
    
    start_time = time.time()
    
    try:
        # Prepare parameters based on model capabilities
        params = {
            "model": model_name,
            "voice": voice,
            "input": f"Hello! This is a test of the {model_name} text-to-speech model. Each model has different capabilities and quality levels.",
            "response_format": "mp3"
        }
        
        # Add instructions only for gpt-4o-mini-tts
        if use_instructions and model_name == "gpt-4o-mini-tts":
            params["instructions"] = "Speak clearly and professionally with a friendly tone."
        
        # Add speed only for tts-1 and tts-1-hd
        if use_speed and model_name in ["tts-1", "tts-1-hd"]:
            params["speed"] = 1.0
        
        with client.audio.speech.with_streaming_response.create(**params) as response:
            response.stream_to_file(speech_file_path)
        
        end_time = time.time()
        generation_time = end_time - start_time
        
        print(f"✅ Success! Generated in {generation_time:.2f} seconds")
        print(f"File size: {speech_file_path.stat().st_size} bytes")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# Test all three models
print("🎵 Testing OpenAI Text-to-Speech Models 🎵")
print("=" * 50)

# Test TTS-1 (basic, fast)
test_tts_model("tts-1", "alloy", "comparison_tts1.mp3", use_instructions=False, use_speed=True)

# Test TTS-1-HD (high quality)
test_tts_model("tts-1-hd", "nova", "comparison_tts1_hd.mp3", use_instructions=False, use_speed=True)

# Test GPT-4o-Mini-TTS (with instructions)
test_tts_model("gpt-4o-mini-tts", "coral", "comparison_gpt4o_mini.mp3", use_instructions=True, use_speed=False)

print("\n" + "=" * 50)
print("🎉 Comparison complete! Check the generated audio files.")
print("\nKey differences:")
print("• TTS-1: Fastest, lower quality, supports speed control")
print("• TTS-1-HD: Higher quality, slower, supports speed control") 
print("• GPT-4o-Mini-TTS: Latest model, supports instructions, no speed control")
