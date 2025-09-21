# Jarvis Voice Assistant

A Python-based voice assistant that can:
- Open websites like Google, YouTube, LinkedIn, and LeetCode  
- Play music from a local music library  
- Respond to commands using Google Gemini AI  

This project is built for learning and personal use. API keys are required for AI and news features.

---

## Features

- Speech recognition with `speech_recognition`  
- Text-to-speech with `pyttsx3`  
- Open web pages directly via voice commands  
- Play songs from your custom music library  
- AI responses using Google Gemini API  

---

## Setup Instructions

### 1. Clone the repository
- git clone https://github.com/devmalik-official/JARVIS---Python-Based-Voice-Assistant.git
cd jarvis-voice-assistant

### 2. Create a virtual environment
- python -m venv venv

### 3. Activate the virtual environment
- Windows CMD: venv\Scripts\Activate
- MAC / Linux: source venv/bin/activate

### 4. Install dependencies
- pip install requirements.txt

### 5. Enter your APIs
- newsapi = "Paste Your News_API Here"
- ai_api = "Paste Your Gemini API Here"

### 6. Run JARVIS
- main.py

## Usage
- Say "Jarvis" to activate the assistant
- Give commands like:
  - Open websites:
    - Google
    - YouTube
    - LinkedIn
    - LeetCode
  - Play songs:
    - "Song1"
    - "Song2"
  - Interact with Google Gemini AI
 
## Notes
- Ensure your microphone works for voice commands.
- Always keep your .env or API key files private.
- The virtual environment folder (venv/) should not be committed to GitHub.
- You can customize the musiclibrary.py file to add more songs or links.




