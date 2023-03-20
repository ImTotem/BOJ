from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)
input = stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

ans = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

cnt = 1
def dfs(node):
    global cnt

    ans[node] = cnt
    cnt += 1

    for x in sorted(graph[node]):
        if not ans[x]:
            dfs(x)

dfs(R)
for i in range(1, N+1):
    print(ans[i])