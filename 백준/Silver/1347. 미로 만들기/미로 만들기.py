import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

def main():
    input()

    d = deque([(0, 1), (-1, 0), (0, -1), (1, 0)])
    log = {(0, 0)}

    r1, r2, c1, c2 = 0, 0, 0, 0
    x, y = 0, 0
    for cmd in input():
        d.rotate(-1 * (cmd == "R") or cmd == "L")
        if cmd == "F":
            x, y = x + d[0][0], y + d[0][1]
            log.add((x, y))
            r1, r2 = min(r1, y), max(r2, y)
            c1, c2 = min(c1, x), max(c2, x)
    
    ans = [[["#", "."][(j, i) in log] for j in range(c1, c2 + 1)] for i in range(r1, r2 + 1)]

    return map(lambda m:''.join(m), ans)

print(*main(), sep="\n")