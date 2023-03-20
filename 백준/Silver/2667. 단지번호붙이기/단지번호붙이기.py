from sys import stdin
input = stdin.readline
from collections import deque

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited = []
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        visited.append([x, y])

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] == 1 and [nx, ny] not in visited and [nx, ny] not in q:
                q.append([nx, ny])
                graph[ny][nx] = 0
    
    return len(visited)

cnt = 0
ans = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            ans.append(bfs(j, i))
            cnt += 1

print(cnt, *sorted(ans), sep="\n")