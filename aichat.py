import time
import random
import datetime

# 현재 시간 및 날짜 가져오기
current_time = datetime.datetime.now()
h = current_time.hour
m = current_time.minute
today = current_time.strftime("%Y-%m-%d")

while True:
    # 사용자에게 질문 입력 받기
    user_input = input("사용자: ")

    # 질문
    if "몇시" in user_input:
        if 6 <= h < 12:
            response = f"{h}시 {m}분! 아침 : 좋은 아침이야 언니!"
        elif 12 <= h < 18:
            response = f"{h}시 {m}분! 점심 : 즐거운 오후!"
        elif 18 <= h < 21:
            response = f"{h}시 {m}분! 저녁 : 벌써 하루가 다 끝나가네"
        elif 21 <= h < 24:
            response = f"{h}시 {m}분! 밤 : 언니 꿈속에서 만나"
        else:
            response = f"{h}시 {m}분! 새벽 : 언니! 왜 아직도 못 자고 있어ㅠㅠㅠ"
    else:
        responses2 = ["원영이는 그런거 몰라", "언니 미안 나 지금 바빠ㅠㅠ 이따 다시 연락 줘!", "대답해주기 싫어 메롱"]
        response = random.choice(responses2)  # 답변할 수 없는 질문에는 이 답변들 중 하나를 랜덤으로 출력

    print("장원영: " + response)

