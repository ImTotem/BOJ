from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
q = deque()
q.append([1, graph[1]])

ans = [0 for _ in range(N+1)]

while q:
    parent, child = q.popleft()
    
    for node in child:
        if not visited[node]:
            q.append([node, graph[node]])
            ans[node] = parent
            visited[node] = True

for i in range(2, N+1):
    print(ans[i])