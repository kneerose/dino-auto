import pyautogui
from PIL import Image,ImageGrab
from numpy import *
from time import sleep
sleep(1)
pyautogui.hotkey('win','r')
sleep(1)
pyautogui.write("chrome")
sleep(1)
pyautogui.press("enter")
sleep(1)
pyautogui.write("chrome://dino")
sleep(1)
pyautogui.press("enter")
sleep(1)
pyautogui.press("up")
sleep(1)

def collide(data):
    for i in range(255,280):
        for j in range(430,463):
            if data[i, j] < 100:
                pyautogui.press("up")
                sleep(0.08)
                pyautogui.press("down")
                return True
            
    for i in range(350, 400):
        for j in range(350, 395):
            if data[i, j] < 100:
                pyautogui.press("down")
                return True
def color():
    for i in range(275,300):
        for j in range(150,200):
            if data[i, j] <100:
                return True

def collide1(data):
     for i in range(255,280):
        for j in range(430,463):
            # if data[150,180]:
            if data[i, j] > 100:
                pyautogui.press("up")
                sleep(0.08)
                pyautogui.press("down")
                return True
     for i in range(350, 400):
        for j in range(350, 395):
            if data[i, j] > 100:
                pyautogui.press("down")
                return True
            
while True:
    image = ImageGrab.grab().convert('L')
    data = image.load()
    if color():
        collide1(data)
            
    else:
        collide(data)
        #     if bird():
#         pyautogui.keyDown("shift")
#         pyautogui.press("down")
#         pyautogui.keyUp("shift")
#         sleep(1)
       
    #     pyautogui.press('down', _pause=2)
#     for i in range(320, 360):
#         for j in range(400, 480):
#             data[i, j] = 0
# sleep(5)
# image=ImageGrab.grab().convert('L')
# data=image.load()
# for i in range(275,300):
#     for j in range(150,200):
#         # if data[150,180]:
#         data[i, j] = 0
# for i in range(350, 400):
#     for j in range(350, 395):
#         data[i, j] = 0
image.show()