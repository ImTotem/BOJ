from bisect import bisect_left
import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
a = list(map(int, input().split()))

dp = [a[0]]

for i in range(n):
    if a[i] > dp[-1]:
        dp.append(a[i])
    else:
        idx = bisect_left(dp, a[i])
        dp[idx] = a[i]

print(len(dp))