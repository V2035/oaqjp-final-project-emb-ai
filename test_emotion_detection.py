"""Unit tests for the emotion detection package."""

import unittest
from unittest.mock import Mock, patch

import requests

from emotion_detection.emotion_detection import API_URL, emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test dominant emotion selection and error handling."""

    @staticmethod
    def response(scores):
        result = Mock()
        result.status_code = 200
        result.json.return_value = {"emotionPredictions": [{"emotion": scores}]}
        result.raise_for_status.return_value = None
        return result

    @patch("emotion_detection.emotion_detection.requests.post")
    def test_dominant_joy(self, post):
        post.return_value = self.response({"anger": .01, "disgust": .01, "fear": .02, "joy": .92, "sadness": .04})
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(post.call_args.args[0], API_URL)

    @patch("emotion_detection.emotion_detection.requests.post")
    def test_dominant_anger(self, post):
        post.return_value = self.response({"anger": .91, "disgust": .02, "fear": .02, "joy": .01, "sadness": .04})
        self.assertEqual(emotion_detector("I am mad") ["dominant_emotion"], "anger")

    @patch("emotion_detection.emotion_detection.requests.post")
    def test_dominant_disgust(self, post):
        post.return_value = self.response({"anger": .02, "disgust": .90, "fear": .02, "joy": .01, "sadness": .05})
        self.assertEqual(emotion_detector("That is disgusting")["dominant_emotion"], "disgust")

    @patch("emotion_detection.emotion_detection.requests.post")
    def test_dominant_fear(self, post):
        post.return_value = self.response({"anger": .02, "disgust": .02, "fear": .91, "joy": .01, "sadness": .04})
        self.assertEqual(emotion_detector("I am afraid")["dominant_emotion"], "fear")

    @patch("emotion_detection.emotion_detection.requests.post")
    def test_dominant_sadness(self, post):
        post.return_value = self.response({"anger": .02, "disgust": .02, "fear": .03, "joy": .01, "sadness": .92})
        self.assertEqual(emotion_detector("I feel sad")["dominant_emotion"], "sadness")

    @patch("emotion_detection.emotion_detection.requests.post")
    def test_blank_input_skips_api(self, post):
        result = emotion_detector("  ")
        self.assertIsNone(result["dominant_emotion"])
        post.assert_not_called()

    @patch("emotion_detection.emotion_detection.requests.post")
    def test_api_failure_is_handled(self, post):
        post.side_effect = requests.RequestException("service unavailable")
        self.assertIsNone(emotion_detector("hello")["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
