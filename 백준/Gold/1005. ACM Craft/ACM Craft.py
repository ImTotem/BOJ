from collections import deque
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())

    D = [0]+list(map(int, input().split()))

    indegree = [0] * (N+1)
    graph = [[] for _ in range(N+1)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    W = int(input())

    q = deque()
    dp = [0] * (N+1)

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = D[i]

    while q:
        cur = q.popleft()

        for i in graph[cur]:
            indegree[i] -= 1

            dp[i] = max(dp[i], D[i] + dp[cur])

            if indegree[i] == 0:
                q.append(i)

    print(dp[W])