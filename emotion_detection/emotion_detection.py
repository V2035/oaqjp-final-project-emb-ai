"""Detect emotions in text using the IBM Watson NLP EmotionPredict API."""

import requests

API_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
EMOTION_NAMES = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result():
    """Return the standard response when input or the API result is invalid."""
    return {**{emotion: None for emotion in EMOTION_NAMES}, "dominant_emotion": None}


def emotion_detector(text_to_analyse):
    """Return five emotion scores and the dominant emotion for input text."""
    if not isinstance(text_to_analyse, str) or not text_to_analyse.strip():
        return _empty_result()

    headers = {
        "grpc-metadata-mm-model-id": MODEL_ID,
        "Content-Type": "application/json",
    }
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"raw_document": {"text": text_to_analyse}},
            timeout=20,
        )
        if response.status_code == 400:
            return _empty_result()
        response.raise_for_status()
        payload = response.json()
        emotions = payload.get("emotionPredictions", [{}])[0].get("emotion", {})
        scores = {emotion: emotions.get(emotion) for emotion in EMOTION_NAMES}
        if any(not isinstance(score, (int, float)) for score in scores.values()):
            return _empty_result()
        scores["dominant_emotion"] = max(EMOTION_NAMES, key=scores.get)
        return scores
    except (requests.RequestException, ValueError, KeyError, IndexError, TypeError):
        return _empty_result()
