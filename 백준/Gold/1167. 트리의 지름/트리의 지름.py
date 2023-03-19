import sys

input = lambda: sys.stdin.readline().strip()

V = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(V):
    a, *b = list(map(int, input().split()))

    for i in range(0, len(b)-1, 2):
        graph[a].append([b[i], b[i+1]])

def dfs(u, wu):
    for v, wv in graph[u]:
        if visited[v] == -1:
            visited[v] = wu + wv
            dfs(v, visited[v])

visited = [-1] * (V+1)
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))

visited = [-1] * (V+1)
visited[start] = 0
dfs(start, 0)

print(max(visited))