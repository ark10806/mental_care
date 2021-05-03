import time
import sys
from random import randint

sp = ' '
strs = '정신나갈것같아'

while True:
    for s in strs:
        print(f'{sp * randint(0,7)}{s}', end='')
        time.sleep(0.05)
        sys.stdout.flush()
    print('\n'*randint(0,3), end='')
    sys.stdout.flush()

