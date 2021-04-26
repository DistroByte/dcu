#!/usr/bin/env python3

import sys

args = sys.argv[1:]

message = "Hello world.\n"
file_name = args[0]

with open(file_name, "w") as f:
    f.write(message)
