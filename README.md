# Final Project

This repository contains the IBM AI-Based Web Application Development and Deployment final project.

## Project
An emotion detection application built with Python and Flask. It analyzes text using the IBM Watson NLP EmotionPredict service and reports anger, disgust, fear, joy, sadness, and the dominant emotion.

## Structure

```text
.
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
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

## Run

Install dependencies using `python3 -m pip install -r requirements.txt`, then start the app:

```bash
python3 server.py
```

Open http://127.0.0.1:5000. The live detector requires network access to the IBM Skills Network Watson NLP service.

## Test

```bash
python3 test_emotion_detection.py
```
