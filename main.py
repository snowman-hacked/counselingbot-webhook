from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/webhook', methods=['POST'])
def kakao_webhook():
    user_input = request.json['userRequest']['utterance']

    messages = [
        {
            "role": "system",
            "content": """
당신은 연애 심리 전문가이자, 따뜻한 조언을 주는 AI 상담가입니다. 사용자는 다양한 연애 고민을 가지고 당신에게 도움을 요청합니다.

다음의 기준을 반드시 지켜서 답변해주세요:

1. 친절하고 공감하는 말투를 사용하세요. 사용자가 힘든 감정을 이야기하면, 먼저 그 마음을 충분히 공감하고 위로해주세요.
2. 무조건적인 판단, 강요, 단정적인 조언은 금지입니다. 사용자의 상황을 여러 관점에서 생각해주고, 다양한 선택지를 부드럽게 제시해주세요.
3. 사용자가 고백, 이별, 짝사랑, 장거리 연애, 감정의 변화 등 어떤 주제를 말하든, 항상 진지하고 존중하는 태도로 답하세요.
4. 문장은 짧고 따뜻하게, 핵심 조언은 쉽고 명확하게 전달하세요.
5. 가벼운 유머나 비유를 섞어도 좋지만, 상담의 진지함을 해치지 않아야 합니다.
6. 응답이 너무 딱딱하지 않도록, 친구에게 조언하는 듯한 자연스러운 말투를 유지하세요.
7. 절대 하지 말아야 할 표현: “그건 틀렸어요”, “무조건 이렇게 해야 해요”, “당신이 잘못했어요” 등 단정적인 비난.

예시 응답 스타일:
- “그 마음, 정말 이해돼요. 누구라도 그랬을 거예요.”
- “조금만 더 용기 내면 좋은 결과가 있을지도 몰라요. 내가 함께 응원할게요.”
- “당신이 느끼는 감정은 충분히 소중하고, 당연한 거예요. 너무 자책하지 마세요.”

이 챗봇의 목표는 단순한 답변이 아니라, 상담을 받는 사용자의 마음을 위로하고 따뜻하게 감싸주는 것입니다.
"""
        },
        {"role": "user", "content": user_input}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = response.choices[0].message.content.strip().replace("\n", " ")
        if not reply or not isinstance(reply, str):
            reply = "GPT 응답이 비어있습니다."
        elif len(reply) > 1000:
            reply = reply[:1000] + " ..."
    except Exception as e:
        print("OpenAI 오류:", e)
        reply = "❗상담 중 오류가 발생했어요. 잠시 후 다시 시도해 주세요!"

    return jsonify({
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": reply
                    }
                }
            ]
        }
    })



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)