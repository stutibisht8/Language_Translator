# Language Translator

A desktop-based Language Translator application built using **Python** and **Tkinter**. This project provides text translation with a simple graphical user interface and includes additional features such as voice input, text-to-speech, copy, save, and language swapping.
---

## Project Overview
The Language Translator is designed to translate text between multiple languages using the Google Translate API. The application features a clean GUI and offers speech-based interaction to improve the user experience.

This project demonstrates Python GUI development, API integration, speech processing, and file handling.

---

## Features

-  Translate text into multiple languages
-  Voice input using Speech Recognition
-  Automatic source language detection
-  Listen to translated text using Text-to-Speech
-  Copy translated text to clipboard
-  Swap input and translated text
-  Save translated text as a `.txt` file
-  Clear input and output instantly
-  User-friendly graphical interface built with Tkinter

---

## Technologies Used

- Python
- Tkinter
- Googletrans
- gTTS (Google Text-to-Speech)
- SpeechRecognition
- SoundDevice
- SoundFile
- NumPy
- PlaySound

---

## Project Structure

```
Language_Translator/
│── language_translator.py
│── background.png
│── README.md
│── .gitattributes
```

---

## Installation

1. Clone the repository

```bash
git clone https://github.com/stutibisht8/Language_Translator.git
```

2. Move to the project folder

```bash
cd Language_Translator
```

3. Install the required libraries

```bash
pip install googletrans==4.0.0rc1
pip install gtts
pip install playsound
pip install SpeechRecognition
pip install sounddevice
pip install soundfile
pip install numpy
```

4. Run the application

```bash
python language_translator.py
```

---

## How to Use
1. Enter text or use the **Voice** button to speak.
2. Select the target language.
3. Click **Translate**.
4. Listen to the translated speech.
5. Copy, Swap, Save, or Clear the translation using the available buttons.

---

## Application Preview

The application includes:
- Clean and modern GUI
- Multi-language translation
- Voice input support
- Text-to-Speech output
- Copy and Save functionality
- Language Swap feature

---

## Learning Outcomes

This project helped in understanding:
- Python GUI Development with Tkinter
- API Integration
- Speech Recognition
- Text-to-Speech Conversion
- File Handling
- Event-driven Programming
- User Interface Design

---

## Future Improvements

- Support for 100+ languages
- Translation History
- Offline Translation
- Pronunciation Speed Control
- Export translation as PDF

---

## Author
**Stuti Bisht**
GitHub: https://github.com/stutibisht8
---
