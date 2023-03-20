from bisect import bisect_left as search
import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())

dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])