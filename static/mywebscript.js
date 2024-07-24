let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    fetch('/emotionDetector', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: textToAnalyze })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("system_response").innerHTML = data.response;
    })
    .catch(error => console.error('Error:', error));
}
