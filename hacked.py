import pyautogui
from time import sleep
import pyttsx3
# sleep(5)
# print(pyautogui.position())
#Point(x=1580, y=30)
# pyautogui.click(x=1493, y=30)
def tts(text):
    eng=pyttsx3.init()
    eng.say(text)

    eng.runAndWait()

def hack_in_process():

    tts("your accound is hacked")
    sleep(2)
    pyautogui.hotkey('win','r')
    sleep(0.3)
    #x=202, y=804
    pyautogui.click(x=202, y=804)
    sleep(0.3)
    pyautogui.hotkey('alt','enter')
    pyautogui.typewrite("color 0a")
    pyautogui.hotkey("enter")
    pyautogui.typewrite("dir/s")
    pyautogui.hotkey("enter")
# # hack_in_process()
