# Reel Masti

Reel Masti is a web application that lets users create Instagram-style reels by uploading images and adding custom text, which is converted to speech using AI. The app automatically stitches images and audio into a video reel.

## Features

- **Text to Speech:** Converts user text to audio using ElevenLabs API.
- **Smart Stitching:** Combines uploaded images into a video reel.
- **Audio Integration:** Adds generated speech to the reel.
- **Gallery:** Browse and play generated reels.

## Project Structure

- `main.py` – Flask web server, handles uploads and gallery.
- `generate_process.py` – Background process to convert uploads into reels.
- `text_to_audio.py` – Text-to-speech conversion logic.
- `config.py` – API key configuration.
- `static/` – CSS, sample songs, and generated reels.
- `templates/` – HTML templates for the web interface.
- `user_uploads/` – Stores user-uploaded files and metadata.
- `done.txt` – Tracks processed folders.

## Getting Started

1. **Install dependencies:**
   ```sh
   pip install flask python-dotenv elevenlabs
   ```
2. **Set your ElevenLabs API key in `config.py`.**
3. **Run the Flask server:**
   ```sh
   python main.py
   ```
4. **Start the background process:**
   ```sh
   python generate_process.py
   ```
5. **Visit `http://localhost:5000` in your browser.**

## Usage

- Go to **Create Reel** to upload images and enter your text.
- Visit **Gallery** to view and play generated reels.

## License
Made with ❤️ by Arshad Ahmed Shaik
