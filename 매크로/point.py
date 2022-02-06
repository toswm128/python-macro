import pyautogui
import random
from datetime import datetime as dt
from PIL import ImageGrab
p=pyautogui
speed=3

p.sleep(speed)
screen = ImageGrab.grab()
# p.click(528,307)
# p.click(1640,228)
po = p.position()



print(p.position(),screen.getpixel(po))