#!/usr/bin/env python3

length, time, pos = int(__import__('sys').stdin.readline()), 0, 0
# This line creates a few variables, length is equal to the first line of the file
# It also defines time and pos to be equal to 0

for line in __import__('sys').stdin:
    # For every line in sys.stdin
    d, r, g = [int(e) for e in line.strip().split()]
    # Unpack each line into integers assigned to d, r and g
    while pos < d + 1:
        # While the current position is less than the position of the current traffic light, plus 1
        pos += 1 if not (pos == d and (time % (r + g)) - r < 0) else 0
        # If the position is the same as the traffic light, and
        # the remainder of red plus green divided by time, minus the red time
        # is less than 0 then advance the position by one
        time += 1
        # advance time by one no matter what
print(time + length - pos)
# Then simply print the time it took to get past all the lights,
# plus the length of the road, minus the current position (which is
# one past the traffic light)


(lambda v, c: (lambda f: f(f, v[1:], None, 0, 0))(lambda f, l, g, s, u: print(s + g - u + int(v[0]) - g) if not l else f(f, l[1:], int(l[0].split()[0]), *c(s, u, *[int(x) for x in l[0].split()]))))(__import__("sys").stdin.readlines(), (lambda t, p, l, r, g: (t + (l - p) + max(0, r - (t + l - p) % (r + g)), l)))