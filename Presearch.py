import pyautogui
import webbrowser
import time
import os

for i in range (30):
    os.system("python3 config.py")
    url = 'https://www.presearch.com/'
    webbrowser.open_new(url)
    time.sleep(3)
    f = open("log.txt", "r") 
    pyautogui.typewrite(f.readline())
    time.sleep(3)
    pyautogui.hotkey('enter')
    time.sleep(5)
os.system("taskkill /im brave.exe /f")