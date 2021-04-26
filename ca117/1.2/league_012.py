#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()


def getClubLen(lines):
    maxClubLen = 0
    for line in lines:
        args = line.split()
        clubName = " ".join(args[1:-8])
        clubLen = len(clubName)
        if clubLen > maxClubLen:
            maxClubLen = clubLen
    return maxClubLen


maxClubLen = getClubLen(lines)
print(f'{"POS":>3s}', f'{"CLUB":{maxClubLen}s}', f'{"P":>2s}', f'{"W":>3s}', f'{"D":>3s}',
      f'{"L":>3s}', f'{"GF":>3s}', f'{"GA":>3s}', f'{"GD":>3s}', f'{"PTS":>3s}')
for line in lines:
    args = line.split()
    clubName = " ".join(args[1:-8])
    print(f'{args[0]:>3s}', f'{clubName:{maxClubLen}s}', f'{args[-8]:>2s}', f'{args[-7]:>3s}',
          f'{args[-6]:>3s}', f'{args[-5]:>3s}', f'{args[-4]:>3s}', f'{args[-3]:>3s}', f'{args[-2]:>3s}',
          f'{args[-1]:>3s}')
