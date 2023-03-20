from sys import stdin
input = stdin.readline
from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(N)]

q = deque()
q.append([0, 0])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

    
        if 0 <= nx < M and 0 <= ny < N and miro[ny][nx] == 1:
            q.append([nx, ny])
            miro[ny][nx] = miro[y][x] + 1

print(miro[N-1][M-1])