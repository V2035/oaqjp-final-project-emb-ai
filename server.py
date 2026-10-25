"""Flask web application for the emotion detector."""

from flask import Flask, jsonify, render_template, request

from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the emotion detection interface."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Analyze query-string text and return a readable result."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    return (
        "For the given statement, the system response is "
        f"anger: {result['anger']}, disgust: {result['disgust']}, "
        f"fear: {result['fear']}, joy: {result['joy']}, "
        f"sadness: {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


@app.route("/api/emotion", methods=["GET"])
def emotion_api():
    """Return emotion scores as JSON for programmatic clients."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyze)
    status = 200 if result["dominant_emotion"] is not None else 400
    return jsonify(result), status


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
