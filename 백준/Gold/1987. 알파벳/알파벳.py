from collections import deque
import sys

input = lambda: sys.stdin.readline().strip()

r, c = map(int, input().split())
a = [list(input()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0
s = {a[0][0]}
def dfs(x, y):
    global ans

    ans = max(ans, len(s))
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < c and 0 <= ny < r and a[ny][nx] not in s:
            s.add(a[ny][nx])
            dfs(nx, ny)
            s.remove(a[ny][nx])


dfs(0, 0)

print(ans)