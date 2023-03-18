import pyautogui
import webbrowser
import time
import os
import random

for i in range (1):
    os.system("python3 config.py")
    url = 'https://www.presearch.com/'
    webbrowser.open_new(url)
    time.sleep(3)
    f = open("log.txt", "r").read().splitlines()
    G = random.choice(f)
    pyautogui.typewrite(G)
    time.sleep(3)
    pyautogui.hotkey('enter')
    time.sleep(5)
os.system("taskkill /im msedge.exe /f")
