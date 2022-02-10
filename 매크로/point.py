import pyautogui
import random
from datetime import datetime as dt
from PIL import ImageGrab
from functools import partial

p=pyautogui
speed=1


# ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


p.sleep(speed)
screen = ImageGrab.grab()
# screen.show()
# p.moveTo(715,331)
# p.click(528,307)
# p.click(1640,228)
# p.scroll(500)
po = p.position()
# p.scroll(-90)



print(p.position(),screen.getpixel(p.position(168*2,138*2)))