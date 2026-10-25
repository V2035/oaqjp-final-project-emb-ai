# AI-Based Web Application Development and Deployment — Emotion Detection

A Flask web application for analyzing text with the IBM Watson NLP EmotionPredict service. It returns scores for **anger**, **disgust**, **fear**, **joy**, and **sadness**, plus the dominant emotion.

## Project structure

```text
.
├── emotion_detection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── server.py
├── requirements.txt
└── test_emotion_detection.py
```

## Setup

Use Python 3.10 or newer. From the repository root, create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
# Windows PowerShell
.venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run the application

```bash
python server.py
```

Open http://127.0.0.1:5000 in your browser, enter a sentence, and select **Run Sentiment Analysis**. The app calls the IBM Watson NLP EmotionPredict service, so the machine needs network access to that service.

## API endpoints

- `GET /` — renders the web interface.
- `GET /emotionDetector?textToAnalyze=I%20am%20happy` — returns a readable emotion summary for the starter frontend.
- `GET /api/emotion?textToAnalyze=I%20am%20happy` — returns the scores as JSON.

Empty input and API errors return a consistent invalid-result response rather than crashing the server.

## Tests

```bash
python -m unittest -v
```

The unit tests mock the external service, so they do not require a live API call.

## Notes

This repository is an educational project based on the IBM Developer Skills Network final-project starter. The live emotion scores depend on availability and behavior of the IBM Skills Network-hosted NLP service.
