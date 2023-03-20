from collections import deque
import sys

input = lambda: sys.stdin.readline().strip()

N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append([0, 0, False, 1])
    visited[0][0][0] = True

    while q:
        x, y, used, an = q.popleft()

        if [x, y] == [M-1, N-1]:
            return an

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx][used]:
                if graph[ny][nx] == 0:
                    q.append([nx, ny, used, an+1])
                    visited[ny][nx][used] = True
                elif not used:
                    q.append([nx, ny, True, an+1])
                    visited[ny][nx][True] = True
    
    return -1

print(bfs())