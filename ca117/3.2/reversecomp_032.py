#!/usr/bin/env python3

import sys


def reverse(words):
    lower = {word.lower(): True for word in words if len(word) >= 5}
    words = [word for word in words if word.lower()[::-1] in lower]
    print(words)


lines = [word.strip() for word in sys.stdin]
reverse(lines)
