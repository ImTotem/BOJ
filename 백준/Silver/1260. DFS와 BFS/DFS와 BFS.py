from sys import stdin
input = stdin.readline
from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

graph = list(map(lambda x:sorted(x), graph))

lid = []
def dfs(v):
    lid.append(v)
    
    for u in graph[v]:
        if u not in lid:
            dfs(u)
    
    return lid

def bfs(v):
    lib = []
    q = deque()
    q.append(v)

    while q:
        v = q.popleft()
        lib.append(v)
        for u in graph[v]:
            if u not in lib and u not in q:
                q.append(u)
    
    return lib

print(*dfs(V))
print(*bfs(V))