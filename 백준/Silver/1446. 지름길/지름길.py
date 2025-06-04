import sys
input = lambda: sys.stdin.readline().strip()
from collections import defaultdict

INF = float('inf')

def main():
    n, d = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(n):
        start, end, cost = map(int, input().split())
        graph[end].append((start, cost))
    
    dp = [0] * (d + 1)
    for i in range(1, d+1):
        dp[i] = dp[i-1] + 1
        for start, cost in graph[i]:
            dp[i] = min(dp[i], dp[start] + cost)

    return dp[d]

if __name__ == "__main__":
    print(main())
