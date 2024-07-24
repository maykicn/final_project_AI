import requests, json


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    myobj = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=myobj, headers=headers)

    response_dict = json.loads(response.text)

    emotion_data = response_dict.get('emotionPredictions', [])[0].get('emotion', {})
    emotion_scores = {emotion: emotion_data.get(emotion, 0.0) for emotion in
                      ['anger', 'disgust', 'fear', 'joy', 'sadness']}

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores