# 💌 GPT 연애상담 챗봇 for KakaoTalk

> 감정을 공감하고, 따뜻한 말로 상담해주는 AI 연애상담 챗봇입니다.  
> 카카오 i 오픈빌더 + OpenAI GPT-3.5 + Flask 기반으로 동작합니다.

---

## 프로젝트 소개

- 사용자가 카카오톡 챗봇에서 연애 고민을 입력하면,  
  OpenAI GPT-3.5 모델을 통해 따뜻한 조언과 공감을 제공합니다.
- 진심어린 답변을 통해 **이별, 고백, 썸, 장거리 연애** 등 다양한 상황에 맞는 상담을 진행합니다.
- 오픈빌더와 Flask를 웹훅으로 연결하여 실시간으로 작동합니다.

---

## 기술 스택

| 항목 | 사용 기술 |
|------|-----------|
| 챗봇 플랫폼 | Kakao i 오픈빌더 |
| 백엔드 | Python 3.11 + Flask |
| AI 모델 | OpenAI GPT-3.5 Turbo API |
| 배포 | Render Web Service |
| 데이터 전송 | JSON (POST) via Webhook |

---

## 프롬프트 세팅 (system message)

```text
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
```

---

## 파일 구성

```
연애상담챗봇
├── app.py                # Flask 웹훅 서버
├── requirements.txt      # 패키지 의존성
└── README.md             # 프로젝트 소개 파일
```

---

## 배포 방법 (Render 기준)

### 1. GitHub 연동 및 Render Web Service 생성

- Render에 로그인 → `New Web Service`
- GitHub 저장소 연결
- Build Command: `pip install -r requirements.txt`
- Start Command: `python main.py`

### 2. 환경 변수 설정

| KEY | VALUE |
|-----|-------|
| `OPENAI_API_KEY` | OpenAI에서 발급받은 키 |
| `PORT` | `5000` (Render에서 자동 지정 가능) |

---

## 오픈빌더 연동

### 1. 카카오 i 오픈빌더 접속: [https://i.kakao.com](https://i.kakao.com)

### 2. 시나리오 설정
- 기본 시나리오에서 웰컴 블록, 폴백 블록에 Webhook 스킬을 사용하고 봇 응답도 스킬사용으로 설정
- 발화 예시: “고백하고 싶어요”, “이별했어요”, “짝사랑 중이에요” 등 다양하게 추가 -> 해도되지만 응답이 스킬(웹훅)이므로 안해도 무관함
- 스킬 타입: Webhook
  - Method: POST  
  - Content-Type: application/json  
  - URL: `https://your-render-url.onrender.com/webhook`

### 3. 웹훅 응답 예시

```json
{
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "simpleText": {
          "text": "그 마음 정말 이해돼요. 누구라도 그랬을 거예요."
        }
      }
    ]
  }
}
```

---

## 주요 기능

- ✅ 연애 관련 모든 발화에 자연어 상담 가능
- ✅ 따뜻하고 공감하는 GPT 기반 프롬프트 설계
- ✅ 오픈빌더와 실시간 연결되는 Flask 서버
- ✅ Render를 통한 무료 배포 가능

---

## 🧯 카카오톡 챗봇 연동 트러블슈팅 정리

---

### ❌ 1. **"fallback 블록으로 넘어감" 현상**

#### 원인
- 사용자의 발화가 시나리오 내 어떤 블록에도 매칭되지 않아서 fallback 처리됨

#### 해결법
- **발화 예시 추가**:  
  `연애상담시작` 블록에 다양한 자연어 예시 추가  
  예: "짝사랑이에요", "이별했어요", "고백해도 될까요?"

- **fallback 블록 → GPT 블록 연결**  
  fallback 블록에서 바로 `GPT상담` 블록으로 연결되도록 시나리오 흐름 구성

---

### ❌ 2. **Webhook 연결은 됐는데 응답이 안 나옴**

#### 원인
- Flask 서버가 JSON 응답 포맷을 잘못 반환하거나  
- `outputs` 구조가 빠짐

#### 해결법
- Flask에서 반환할 때 반드시 아래 구조로 반환:

```json
{
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "simpleText": {
          "text": "GPT 응답 텍스트"
        }
      }
    ]
  }
}
```

- `reply = GPT 응답` 변수 확인 후 `.strip()` 으로 공백 제거 필수

---

### ❌ 3. **GPT 호출 시 오류 발생 (OpenAI API 관련)**

#### 에러 메시지 예시

```
You tried to access openai.ChatCompletion, but this is no longer supported in openai>=1.0.0
```

#### 해결법
- `openai` 최신 버전(1.0 이상)에 맞게 코드 수정

```python
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
response = client.chat.completions.create(...)
```

또는 `pip install openai==0.28` 로 버전 다운 (비추천)

---

### ❌ 4. **Render 배포는 됐는데 응답이 “❗오류가 발생했어요”만 뜸**

#### 원인
- 실제 GPT 응답 오류 발생 시 fallback 메시지 출력됨  
- 서버에서 try-except 블록에서 예외 발생 시 `"❗GPT 응답 중 오류 발생"`으로 응답되도록 처리됨

#### 해결법
- Render의 `Logs` 탭 확인  
- 오류 메시지 직접 보기 위해 Flask 코드에 `print("❗GPT 응답 오류:", e)` 삽입
- `reply = f"❗GPT 오류 발생: {str(e)}"`로 사용자에게도 전달

---

### ❌ 5. **카카오톡 채널에서 시나리오가 작동하지 않음**

#### 원인
- 챗봇을 **비즈니스센터에서 만든 경우** 오픈빌더가 아님
- 오픈빌더와 연결되지 않아서 웹훅 사용 불가능

#### 해결법
- [https://i.kakao.com](https://i.kakao.com) → 챗봇 새로 생성
- **카카오톡 채널 연동 필수**
- 오픈빌더 안에서 시나리오, 블록, 스킬 설정 진행

---

### ❌ 6. **Webhook 테스트는 되는데 실제 발화에선 실패함**

#### 원인
- 발화 예시는 입력됐지만, 블록 간 연결이 없음
- 혹은 블록 안에 **Webhook 스킬이 없거나 잘못된 URL 입력**

#### 해결법
- `GPT상담` 블록 안에 Webhook 스킬 정확히 설정
- POST / application/json / 정확한 Render URL 입력
- 시나리오 흐름에서 해당 블록으로 연결되었는지 확인
