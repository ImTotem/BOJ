from collections import deque

import sys
input = lambda:sys.stdin.readline().strip()

direction = deque(["N", "E", "S", "W"])

for _ in range(10):direction.rotate([0, -1, -2, 1][int(input())])
print(direction[0])