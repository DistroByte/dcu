#!/usr/bin/env python3

def reverse_list(toRev):
    return [toRev[-1]] + reverse_list(toRev[:-1]) if toRev else []
