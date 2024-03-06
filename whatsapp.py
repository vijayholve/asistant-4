import pyautogui
import webbrowser as wb
from time import sleep
# sleep(6)
# print(pyautogui.position())
persons=["vijay","jio","eatclub"]
def open_whatsapp(person,msg):
    
    wb.open("https://web.whatsapp.com/")
    sleep(7)
    
    # pyautogui.hotkey("F11")
    sleep(1)
    # print(pyautogui.position())
    pyautogui.click(x=116, y=172)

    pyautogui.typewrite(person)
    sleep(1)
    pyautogui.click(x=120, y=296)
    pyautogui.click(x=615, y=845)
    pyautogui.typewrite(msg)
    pyautogui.hotkey("enter")
    pyautogui.hotkey("alt","tab")
    