from sys import stdin
input = stdin.readline
from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start = [[x, y] for y in range(N) for x in range(M) if graph[y][x] == 1]

q = deque()
q.extend(start)

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 0:
            q.append([nx, ny])
            graph[ny][nx] = graph[y][x] + 1

flat = sum(graph, [])

print([max(flat) - 1, -1][0 in flat])