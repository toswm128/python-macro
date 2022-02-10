import pyautogui as p
import json
import random
from datetime import datetime as dt
from PIL import ImageGrab

with open('id.json') as json_file:
    json_data = json.load(json_file)

ids = json_data['idList']

speed = 1

for i in ids:
    print(i)
    p.click(1146,104) # 로그인 클릭
    p.sleep(speed)
    p.click(377,345) # 로그인 - 아이디 클릭
    p.sleep(0.2)
    p.write(i) # 로그인 - 아이디 입력
    p.sleep(speed)
    p.click(429,418) #로그인 - 비밀번호 클릭
    p.sleep(0.2)
    p.write('cb0916!') # 로그인 - 비밀번호 입력
    p.sleep(speed)
    p.click(497,522) # 로그인 - 로그인 버튼
    p.sleep(speed)
    p.click(530,347) # 투표 클릭
    p.sleep(speed)
    p.scroll(-90) # 스크롤
    p.sleep(speed)
    p.click(600,555) #투표하기
    p.sleep(speed)
    p.click(623,762) # 투표 자동입력 방지 문자 누르기
    p.sleep(1)
    while(True):
        screen = ImageGrab.grab()
        if screen.getpixel(p.position(715*2,331*2)) == (93, 153, 252, 255):
            p.click(584,549)
            break
        p.sleep(1)
    p.sleep(1)
    p.click(331,296) # 본인인증하기
    p.sleep(speed)
    p.click(425,549) #전체 동의
    p.sleep(speed)
    p.click(601,658) # pass 인증
    p.sleep(speed)
    p.click(739,526)
    p.sleep(1)
    while(True):
        screen = ImageGrab.grab()
        if screen.getpixel(p.position(168*2,138*2)) == (245, 137, 128, 255):
            p.hotkey('command','w')
            break
        p.sleep(1)
    p.sleep(speed)
    p.scroll(500)
    p.sleep(speed)
    p.click(1139,101)
    p.sleep(0.5)
    p.click(1139,101)
    p.sleep(speed)
    p.sleep(speed)






