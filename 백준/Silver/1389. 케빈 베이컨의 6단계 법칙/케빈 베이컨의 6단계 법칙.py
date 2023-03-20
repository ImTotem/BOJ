from sys import stdin
input = stdin.readline
from collections import deque

N, M = map(int, input().split())

g = [[float("inf") if i != j else 0 for i in range(N)] for j in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u][v] = 1
    g[v][u] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

f = list(map(sum, g))
print(f.index(min(f))+1)