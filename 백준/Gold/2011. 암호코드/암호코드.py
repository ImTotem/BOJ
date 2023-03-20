import sys

input = lambda: sys.stdin.readline().strip()

n = '0'+input()

l = len(n)

dp = [0] * l
dp[0] = 1

for i in range(1, l):
    if n[i] != '0':
        dp[i] = dp[i-1]

    if n[i-1] != '0' and 1 <= int(n[i-1]+n[i]) <= 26:
        dp[i] = dp[i] + dp[i-2]
    
print(dp[l-1]%1000000)