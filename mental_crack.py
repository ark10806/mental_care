import time
from random import randint
import pyautogui as auto

noRand = True

time.sleep(1.0)
while(True):
    auto.press('w')
    auto.press('j')
    auto.press('d')
    if(randint(0,1) or noRand):
        auto.press('enter')
    auto.press('t')
    auto.press('l')
    auto.press('s')
    if(randint(0,1) or noRand):
        auto.press('enter')
    auto.press('s')
    auto.press('k')
    if(randint(0,1) or noRand):
        auto.press('enter')
    auto.press('r')
    auto.press('k')
    auto.press('f')
    if(randint(0,1) or noRand):
        auto.press('enter')
    auto.press('r')
    auto.press('j')
    auto.press('t')
    if(randint(0,1) or noRand):
        auto.press('enter')
    auto.press('r')
    auto.press('k')
    auto.press('x')
    if(randint(0,1) or noRand):
        auto.press('enter')
    auto.press('d')
    auto.press('k')
    auto.press('enter')