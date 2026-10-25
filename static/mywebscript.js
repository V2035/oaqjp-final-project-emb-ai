"use strict";

const RunSentimentAnalysis = async () => {
    const input = document.getElementById("textToAnalyze");
    const output = document.getElementById("system_response");
    const textToAnalyze = input.value.trim();

    if (!textToAnalyze) {
        output.textContent = "Please enter some text to analyze.";
        return;
    }

    output.textContent = "Analyzing...";
    try {
        const response = await fetch(
            `/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`
        );
        const result = await response.text();
        output.textContent = result;
    } catch (error) {
        output.textContent = "Unable to contact the server. Please try again.";
    }
};
