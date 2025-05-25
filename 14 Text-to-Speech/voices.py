# Voice Testing Script - Generate audio samples for all available voices
from pathlib import Path
from openai import OpenAI
import time

client = OpenAI()

# All available voices according to OpenAI documentation
AVAILABLE_VOICES = [
    "alloy", "ash", "ballad", "coral", "echo", 
    "fable", "onyx", "nova", "sage", "shimmer", "verse"
]

def generate_voice_sample(voice_name):
    """Generate an audio sample for a specific voice"""
    speech_file_path = Path(__file__).parent / f"voice_sample_{voice_name}.mp3"
    
    # Custom message for each voice
    input_text = f"This is how {voice_name} sounds when you use it to produce audio."
    print(f"🎤 Generating sample for voice: {voice_name}")
    
    start_time = time.time()
    
    try:
        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",  # Using gpt-4o-mini-tts to test all voices
            voice=voice_name,
            input=input_text,
            response_format="mp3"
            # Note: speed parameter doesn't work with gpt-4o-mini-tts
        ) as response:
            response.stream_to_file(speech_file_path)
        
        end_time = time.time()
        generation_time = end_time - start_time
        file_size = speech_file_path.stat().st_size
        
        print(f"✅ {voice_name}: Generated in {generation_time:.2f}s ({file_size} bytes)")
        return True
        
    except Exception as e:
        print(f"❌ {voice_name}: Error - {e}")
        return False

def generate_all_voices():
    """Generate audio samples for all available voices"""
    print("🎵 Voice Sample Generator 🎵")
    print("=" * 50)
    print(f"Generating samples for {len(AVAILABLE_VOICES)} voices using GPT-4o-Mini-TTS model")
    print("=" * 50)
    
    successful = 0
    failed = 0
    
    start_total = time.time()
    
    for voice in AVAILABLE_VOICES:
        if generate_voice_sample(voice):
            successful += 1
        else:
            failed += 1
        
        # Small delay to avoid rate limiting
        time.sleep(0.5)
    
    end_total = time.time()
    total_time = end_total - start_total
    
    print("\n" + "=" * 50)
    print("🎉 Voice sample generation complete!")
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"⏱️ Total time: {total_time:.2f} seconds")
    print("\n📁 Generated files:")
    
    # List generated files
    for voice in AVAILABLE_VOICES:
        file_path = Path(__file__).parent / f"voice_sample_{voice}.mp3"
        if file_path.exists():
            print(f"   • voice_sample_{voice}.mp3")

def generate_single_voice(voice_name):
    """Generate a sample for a single voice"""
    if voice_name not in AVAILABLE_VOICES:
        print(f"❌ Error: '{voice_name}' is not a valid voice.")
        print(f"Available voices: {', '.join(AVAILABLE_VOICES)}")
        return
    
    print(f"🎤 Generating single voice sample for: {voice_name}")
    print("=" * 50)
    
    generate_voice_sample(voice_name)

if __name__ == "__main__":
    # You can modify this to test specific voices or all voices
    
    # Option 1: Generate samples for all voices
    generate_all_voices()
    
    # Option 2: Generate sample for a specific voice (uncomment to use)
    # generate_single_voice("coral")
    
    # Option 3: Generate samples for a few selected voices (uncomment to use)
    # selected_voices = ["alloy", "nova", "coral", "onyx"]
    # print(f"🎤 Generating samples for selected voices: {', '.join(selected_voices)}")
    # for voice in selected_voices:
    #     generate_voice_sample(voice)
    #     time.sleep(0.5)
