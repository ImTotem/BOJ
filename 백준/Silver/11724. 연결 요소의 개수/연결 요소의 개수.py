from sys import stdin
input = stdin.readline
from collections import deque

def bfs(u):
    li = []
    q = deque()
    q.append(u)

    while q:
        x = q.popleft()

        li.append(x)
        for v in graph[x]:
            if v not in li and v not in q:
                q.append(v)
    
    return li


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

cnt = 0
visited = []
for u in range(1, N+1):
    if u not in visited:
        visited += bfs(u)
        cnt += 1

print(cnt)