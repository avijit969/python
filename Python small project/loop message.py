import pyautogui
import time
import random

time.sleep(5)
words = ['kn', 'puni kn', 'aare kn', 'kn re']
for a in range(10):
    pyautogui.typewrite(f"eita {random.choice(words)}")
    # time.sleep(5)
    pyautogui.press("enter")
