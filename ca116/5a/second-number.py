#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and (s[i] <= "0" or "9" <= s[i]):
    i += 1

j = i
if i < len(s):
    while j < len(s) and ("0" <= s[j] or s[j] >= "9"):
        j += 1

m = j
if j < len(s):
    while m < len(s) and (s[m] < "0" or "9" < s[m]):
        m += 1

k = m
if m < len(s):
    while k < len(s) and ("0" <= s[k] or s[k] >= "9"):
        k += 1

if m < len(s):
    print(s[m:k], m)
