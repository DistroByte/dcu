#!/usr/bin/env python3

import sys

nums = [line.split() for line in sys.stdin]

numSet = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
          5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
          10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
          14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
          17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = ['twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety']

for line in nums:
    toPrint = []
    for strNum in line:
        try:
            num = int(strNum)
            if num <= 19 and num >= 0:
                toPrint.append(numSet[num])
            elif num <= 99:
                if num % 10 != 0:
                    toPrint.append(tens[int(strNum[0]) - 2] + "-" +
                                   numSet[int(strNum[-1:])])
                else:
                    toPrint.append(tens[int(strNum[0]) - 2])
            elif num == 100:
                toPrint.append('one hundred')
        except ValueError:
            toPrint.append("unknown")

    print(" ".join(toPrint))
