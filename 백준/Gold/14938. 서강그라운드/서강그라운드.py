import sys
input = lambda:sys.stdin.readline().strip()

n, m, r = map(int, input().split())

t = list(map(int, input().split()))

graph = [[[0, float("inf")][i!=j] for i in range(n)] for j in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    a, b = (a-1, b-1)

    graph[a][b] = l
    graph[b][a] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

ans = 0
for i in range(n):
    tmp = sum( t[j] if graph[i][j] <= m else 0 for j in range(n) )
    ans = max(ans, tmp)

print(ans)
