from collections import deque
import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())

q = deque()

campus = []

for i in range(n):
    line = input()
    campus.append(list(line))
    if 'I' in line:
        q.append((line.index('I'), i))
        campus[q[0][1]][q[0][0]] = 'X'

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0
while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and campus[ny][nx] != 'X':
            q.append((nx, ny))
            if campus[ny][nx] == 'P': ans += 1

            campus[ny][nx] = 'X'

print(['TT', ans][0 < ans])
