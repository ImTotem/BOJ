from collections import deque
from sys import stdin
input = stdin.readline

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

start = []
for h in range(H):
    for y in range(N):
        for x in range(M):
            if graph[h][y][x] == 1:
                start.append([h, x, y])

q = deque()
q.extend(start)

while q:
    h, x, y = q.popleft()

    for i in range(6):
        nh, nx, ny = h + dh[i], x + dx[i], y + dy[i]

        if 0 <= nh < H and 0 <= nx < M and 0 <= ny < N and graph[nh][ny][nx] == 0:
            q.append([nh, nx, ny])
            graph[nh][ny][nx] = graph[h][y][x] + 1
    
flat = sum(sum(graph, []), [])
print(-1 if 0 in flat else max(flat)-1)