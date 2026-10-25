"""Detect emotions using the IBM Watson NLP EmotionPredict service."""

import requests

API_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def _invalid_result():
    """Return a consistent result for blank or invalid input."""
    return {**{name: None for name in EMOTIONS}, "dominant_emotion": None}


def emotion_detector(text_to_analyse):
    """Return emotion scores and the dominant emotion for the supplied text."""
    if not isinstance(text_to_analyse, str) or not text_to_analyse.strip():
        return _invalid_result()

    headers = {"grpc-metadata-mm-model-id": MODEL_ID}
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"raw_document": {"text": text_to_analyse}},
            timeout=20,
        )
        if response.status_code == 400:
            return _invalid_result()
        response.raise_for_status()
        payload = response.json()
        emotion_data = payload["emotionPredictions"][0]["emotion"]
        scores = {name: emotion_data.get(name) for name in EMOTIONS}
        if any(not isinstance(value, (int, float)) for value in scores.values()):
            return _invalid_result()
        scores["dominant_emotion"] = max(EMOTIONS, key=scores.get)
        return scores
    except (requests.RequestException, ValueError, KeyError, IndexError, TypeError):
        return _invalid_result()
