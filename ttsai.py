from gtts import gTTS
import os

# 사용자로부터 언어 선택 입력
language_option = input("음성 변환 언어 선택 (한국어: ko, 영어: en, 일본어: ja): ")

user_input = input("인사해 주세요! : ")

if language_option == "ko":
    if user_input == "사쿠라":
        response = "지금은 안돼"
    else:
        response = "뭐라고?"

elif language_option == "en":
    if user_input == "Sakura":
        response = "Not now"
    else:
        response = "what?"

elif language_option == "ja":
    if user_input ==  "咲良":
       response = "今はできません。"
    else:
        response = "に"

else:
    response = "지원하지 않는 언어입니다."

# 텍스트를 음성으로 변환
tts = gTTS(text=response, lang=language_option)

# 음성을 파일로 저장
tts.save("response.mp3")

# 저장된 음성파일 재생
os.system("mpg321 response.mp3")
