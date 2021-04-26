#!/usr/bin/env python3

s = input()
i = 0
d = 0
wd = 0
m = 0
y = 0

while i < len(s):
    if ("0" <= s[i] and s[i] <= "9") and i < 15:
        if ("0" <= s[i + 1] and s[i + 1] <= "9") and i < 15:
            d = s[i: i + 4]
            wd = s[0: i - 1]
            m = s[i + 5:s.index(",")]
            y = s[s.index(",") + 2:len(s)]
            i += 4
        else:
            d = s[i: i + 3]
            wd = s[0: i - 1]
            m = s[i + 4:s.index(",")]
            y = s[s.index(",") + 2:len(s)]
            i += 3

    i += 1

print(m, d + ",", y, "(" + wd + ")")
