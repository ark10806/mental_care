import pyautogui as auto
import time

time.sleep(1.0)
term = 0.1
while(True):
    auto.click()
    time.sleep(term)
    auto.press('f5')
    time.sleep(term)