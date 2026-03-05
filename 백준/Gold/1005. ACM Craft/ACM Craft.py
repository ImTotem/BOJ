import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush
from collections import deque

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        deg[y] += 1

    w = int(input())
    
    q = deque()
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if deg[i] != 0: continue
        q.append(i)
        dp[i] = d[i]
    
    while q:
        x = q.popleft()

        for y in graph[x]:
            deg[y] -= 1

            dp[y] = max(dp[y], dp[x] + d[y])

            if deg[y] == 0:
                q.append(y)

    return dp[w]

if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
