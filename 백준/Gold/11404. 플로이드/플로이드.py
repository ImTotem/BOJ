INF = float("inf")
from sys import stdin
input = stdin.readline

n = int(input())
m = int(input())

graph = [[[0, INF][i!=j] for j in range(n)] for i in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(n):
    for j in range(n):
        graph[i][j] = graph[i][j] if graph[i][j] != INF else 0
    
    print(*graph[i])