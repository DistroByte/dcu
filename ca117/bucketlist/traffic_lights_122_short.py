l, pos, t = int(__import__("sys").stdin.readline()), 0, 0

[print((lambda x, pos, t: (lambda d, r, g: (t + (d - pos)) + (t % (r + g)) if t % (r + g) < r else 0)(int(line.split()[0]), int(line.split()[1]), int(line.split()[2])) for line in __import__("sys").stdin))]


# print((lambda l, pos, t: (t + l - pos))(int(__import__("sys").stdin.readline()), 0, 0))