from sys import stdin
input = stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    pos = deque(list(map(int, input().split())) for _ in range(K))

    cnt = 0

    wait = deque()

    while pos:
        p = pos.popleft()
        wait.append(p)

        while wait:
            x, y = wait.popleft()

            x1, x2 = x - 1, x + 1
            y1, y2 = y - 1, y + 1

            a, b, c, d = [x1, y], [x2, y], [x, y1], [x, y2]

            for cord in a, b, c, d:
                if cord in pos:
                    wait.append(cord)
                    pos.remove(cord)
        cnt += 1

    print(cnt)