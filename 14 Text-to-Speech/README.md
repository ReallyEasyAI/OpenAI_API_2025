# OpenAI Text-to-Speech Demo

This project demonstrates how to use the OpenAI API to generate speech audio files from text using different models, voices, and settings.

## Features
- Generate speech using all available OpenAI TTS voices
- Compare TTS models: `tts-1`, `tts-1-hd`, and `gpt-4o-mini-tts`
- Test different speech speeds
- Easily extendable for new voices or models

## Requirements
- Python 3.8+
- An OpenAI API key (set as the environment variable `OPENAI_API_KEY` or in a `.env` file)

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Generate Speech for All Voices
```
python voices.py
```
Generates an audio sample for each available voice using the latest model.

### Compare Models
```
python compare_models.py
```
Generates audio samples using all three TTS models for comparison.

### Test Speech Speeds
```
python speed.py
```
Generates three files: normal, double, and half speed.

### Generate Speech for a Single Voice
Uncomment the relevant line in `voices.py`:
```
# generate_single_voice("coral")
```

## Output
- All generated `.mp3` files are ignored by git (see `.gitignore`).
- Listen to the output files to compare voices, models, and speeds.

## Notes
- Some voices may only be available with certain models (e.g., `ballad` and `onyx` with `gpt-4o-mini-tts`).
- The OpenAI API may have rate limits; the scripts include small delays to avoid hitting them.

## License
MIT
