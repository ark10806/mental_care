import time
from random import randint
import pyautogui as auto

noRand = True
width = 30

time.sleep(1.0)
while(True):
    for _ in range(width):
        auto.hotkey('ctrl', 'a')
        auto.hotkey('ctrl', 'c')
        auto.press('enter')
        auto.hotkey('ctrl', 'v')
        auto.hotkey('shift', '8')
    
    for _ in range(width):
        auto.hotkey('ctrl', 'a')
        auto.hotkey('ctrl', 'c')
        auto.press('enter')
        auto.hotkey('ctrl', 'v')
        auto.press('backspace')

    # for i in range(width):
    #     for _ in range(i+1):
    #         auto.hotkey('control', 'a')
    #         auto.hotkey('control', 'c')
    #         auto.press('enter')
    #         auto.hotkey('control', 'v')
    #         auto.hotkey('shift', '8')
    #         # auto.press('d')
    #     auto.press('enter')

    # for i in range(width):
    #     for _ in range(width-i):
    #         auto.hotkey('shift', '8')
    #         # auto.press('d')
    #     auto.press('enter')
    # auto.press('w')
    # auto.press('j')
    # auto.press('d')
    # if(randint(0,1) or noRand):
    #     auto.press('enter')
    # auto.press('t')
    # auto.press('l')
    # auto.press('s')
    # if(randint(0,1) or noRand):
    #     auto.press('enter')
    # auto.press('s')
    # auto.press('k')
    # if(randint(0,1) or noRand):
    #     auto.press('enter')
    # auto.press('r')
    # auto.press('k')
    # auto.press('f')
    # if(randint(0,1) or noRand):
    #     auto.press('enter')
    # auto.press('r')
    # auto.press('j')
    # auto.press('t')
    # if(randint(0,1) or noRand):
    #     auto.press('enter')
    # auto.press('r')
    # auto.press('k')
    # auto.press('x')
    # if(randint(0,1) or noRand):
    #     auto.press('enter')
    # auto.press('d')
    # auto.press('k')
    # auto.press('enter')