import pyautogui
import json
import random
from datetime import datetime as dt
from PIL import ImageGrab

with open('id.json') as json_file:
    json_data = json.load(json_file)

p = pyautogui
p.sleep(2)

speed = 1.5

start = 0
end = 0
password = 'fromis9!!'
server = 'http://192.168.219.109:5000/m'

ids = json_data['idList']
po = p.position()


# def postM(i,j):
#     requests.post(url=server)

# asyncio.run(postM(1,2))

# postM(1,2)

for i,j in zip(ids,range(1,len(ids))):
    start = dt.now()
    speed = round(random.uniform(1.5, 3),1)
    print(speed,'속도')
    print(len(ids),'남은 개수')
    print(i,'이번계정')
    print(j,'번째')
    p.click(1212,675) #알람 허용
    p.sleep(speed)
    p.click(1773,981)#슬라이드 1
    p.sleep(0.5)
    p.click(1773,981)#슬라이드 2
    p.sleep(0.5)
    p.click(1773,981)#슬라이드 3
    p.sleep(0.5)
    p.click(1773,981)#슬라이드 4
    p.sleep(0.5)
    p.click(1773,981)#시작하기
    p.sleep(0.5)
    p.click(1773,981)#마이페이지
    p.sleep(speed)
    p.click(528,307)#로그인 클릭
    p.sleep(speed)
    p.scroll(-500)  # 스크롤
    p.sleep(speed)
    p.write('t')#카카오톡 로그인
    p.sleep(1)
    while(True):
        screen = ImageGrab.grab()
        if screen.getpixel(p.position(841,546)) == (246,246,246):
            p.click(277,312)#이메일 입력 클릭
            break
        p.sleep(1)
    p.sleep(0.2)
    p.write(i)
    p.sleep(speed)
    p.click(158,448) #비밀번호 입력 클릭
    p.sleep(0.2)
    p.write(password)
    p.sleep(speed)
    p.click(965,578) #로그인 제출
    p.sleep(1)
    while (True):
        screen = ImageGrab.grab()
        if screen.getpixel(p.position(370, 186)) == (255, 146, 188):
            p.click(326, 327) #전체동의
            break
        p.sleep(1)
        print(2)
    p.sleep(speed)
    p.click(951,828)
    p.sleep(speed)
    p.click(904,580)
    p.sleep(1)
    while(True):
        screen = ImageGrab.grab()
        if screen.getpixel(p.position(1392,966)) == (255, 177, 181):
            p.sleep(1)
            p.click(1758,242) # 약관 1
            break
        p.sleep(1)
        print(3)
    p.sleep(speed)
    p.click(1754,540) #약관 2
    p.sleep(speed)
    p.click(1780,986) #다음
    p.sleep(1)
    while(True):
        screen = ImageGrab.grab()
        if screen.getpixel(p.position(1356,452)) == (156,152,202):
            p.click(1640,228) #모달 제거 문제지점
            break
        p.sleep(1)
        print(4)
    p.sleep(speed)
    p.click(470,446) # 검색 클릭
    p.sleep(0.2)
    p.write('fro') #프로미스나인 타ㅣ핑
    p.sleep(speed)
    p.click(1727,457) #검색
    p.sleep(speed)
    p.click(354,666) #프로미스 선택
    p.sleep(speed)
    p.click(1780, 986) #다음
    p.sleep(speed)
    p.click(1780, 986)  # 시작하기
    # p.sleep(5)
    # p.write('m') # 닫기 모달클릭 시t
    p.sleep(speed)
    p.click(1280,978) #별 클릭
    p.sleep(1)
    p.scroll(-500) #스크롤 1
    p.sleep(1)
    p.scroll(-500) #스크롤 2
    p.sleep(1)
    p.click(929,982) #참여하기
    p.sleep(speed)
    p.write('m') #마켓
    p.sleep(1)
    while(True):
        screen = ImageGrab.grab()
        if screen.getpixel(p.position(153,523)) == (254,241,103):
            p.click(1737,403) #받기
            break
        p.sleep(1)
        print(5)
    p.sleep(1)
    p.click(894,963) #받기 하단
    p.sleep(speed)
    p.write('t') #교환하기 모달
    p.sleep(1)
    p.write('t') #교환 모달 확인
    p.sleep(speed)
    p.write('b') #뒤로가기
    p.sleep(speed)
    p.write('t')  #투표하기m
    p.sleep(1)
    # for j in range(6):
    #     print(j)
    #     p.hotkey('ctrl', 'down')
    #     p.sleep(0.5)
    # p.sleep(speed)
    # p.click(1745,885)# 중요 @@@@@@@@@ 투표 하는곳 현재 2등임
    while (True):
        screen = ImageGrab.grab()
        if screen.getpixel(p.position(1746,776)) == (58,85,168):
            p.click(1737,803) #중요 @@ 현재 1등
            break
        p.sleep(1)
        print(6)
    p.sleep(speed)
    p.write('t') #투표하기 모달
    p.sleep(speed)
    # p.click(1090,316) #공유 모달 제거
    # p.sleep(speed)
    # p.click(627,100) #뒤로가기
    # p.sleep(speed)
    # p.click(1139,995) #마이페이지
    # p.sleep(speed)
    # p.click(951,369)
    # p.sleep(speed)
    # p.click(1101,972)
    # p.sleep(speed)
    p.click(719,18) # 설정
    p.sleep(speed)
    p.click(426,659) #데이터 지우기
    p.sleep(speed)
    p.click(1320,656) #데이터 지우기 모달
    p.sleep(speed)
    p.click(542,24) #후즈팬 열기
    p.sleep(speed)
    p.sleep(speed)
    end = dt.now()
    # postM(i,j)
    print(end-start)
print(p.position())


