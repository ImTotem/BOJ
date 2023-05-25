from collections import deque
from copy import deepcopy as copy
import sys
input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())

area = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    test = copy(area)

    que = deque()
    
    for i in range(n):
        for j in range(m):
            if test[i][j] == 2:
                que.append((j, i))

    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and test[ny][nx] == 0:
                    test[ny][nx] = 2
                    que.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            cnt += [0, 1][test[i][j] == 0]
    
    return cnt

ans = 0

def dfs(cnt):
    global ans

    if cnt == 3:
        ans = max(ans, bfs())
        return
    
    for i in range(n):
        for j in range(m):
            if area[i][j] == 0:

                area[i][j] = 1
                dfs(cnt+1)
                area[i][j] = 0

dfs(0)
print(ans)