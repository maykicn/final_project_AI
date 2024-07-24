"""Flask web application for emotion detection"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """
    Render the index page
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detection():
    """
    Handle emotion detection requests
    """
    try:
        data = request.json
        text_to_analyse = data['text']
        result = emotion_detector(text_to_analyse)
        if result['dominant_emotion'] is None:
            return jsonify({"response": "Invalid text! Please try again."})
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']},"
            f"'fear': {result['fear']},"
            f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return jsonify({"response": response_text})
    except KeyError as e:
        print(f"KeyError: {e}")
        return jsonify({"error": f"Key error: {str(e)}"}), 400
    except ValueError as e:
        print(f"ValueError: {e}")
        return jsonify({"error": f"Value error: {str(e)}"}), 400
    except TypeError as e:
        print(f"TypeError: {e}")
        return jsonify({"error": f"Type error: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
