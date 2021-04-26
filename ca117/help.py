#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isLoopbackDetected' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts INTEGER_ARRAY packetCounts as parameter.
#

def isLoopbackDetected(packetCounts):
    # Write your code here
    # packets = [packet for packet in packetCounts if packet != 0]
    # return len(packets) != len(set(packets))
    for packet in packetCounts:
        if packetCounts.count(packet) == 2 and packet != 0:
            return 1
    return 0


if __name__ == '__main__':
    packetCounts_count = int(input().strip())

    packetCounts = []

    for _ in range(packetCounts_count):
        packetCounts_item = int(input().strip())
        packetCounts.append(packetCounts_item)

    result = isLoopbackDetected(packetCounts)
    print(result)
