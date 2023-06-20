from collections import deque
import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
land = []

q = deque()
visited = [[-1] * m for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    
    if 2 in line:
        q.append((line.index(2), i))
        visited[q[0][1]][q[0][0]] = 0
    
    land.append(line)
    
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1 and land[ny][nx] != 0:
            visited[ny][nx] = visited[y][x]+1

            q.append((nx, ny))

for i in range(n):
    for j in range(m):
        print([visited[i][j], 0][land[i][j] == 0], end=' ')
    print()