import sys

input = lambda: sys.stdin.readline().strip()

INF = float('inf')

n = int(input())
a = list(map(int, input().split()))

dp = [0] + [INF] * (n-1)

for i in range(n):
    for j in range(a[i]):
        if i + j + 1 < n:
            dp[i+j+1] = min(dp[i+j+1], dp[i] + 1)

print(
    [ -1, dp[-1] ] [ dp[-1] != INF ]
)