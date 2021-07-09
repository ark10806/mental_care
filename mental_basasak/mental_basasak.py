import time
import sys
from random import randint

sp = ' '
strs = '정신나갈것같아'

while True:
    print('\t'*randint(0,5), end='')
    sys.stdout.flush()
    for s in strs:
        print(f'{sp * randint(0,7)}{s}', end='')
        time.sleep(0.02)
        sys.stdout.flush()
    print('\n'*randint(0,6), end='')
    sys.stdout.flush()

