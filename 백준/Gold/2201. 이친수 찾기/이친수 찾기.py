import sys

input = lambda: sys.stdin.readline().strip()

K = int(input())

dp = [0] * (88)
dp[1] = 1
dp[2] = 2
dp[3] = 3

length = 0
if K < 4:
    length = dp[K]
else:
    for i in range(3, 88):
        dp[i] = dp[i-1] + dp[i-2]

        if K < dp[i]:
            length = i-1
            break

ans = ''

for i in range(length):
    if dp[length - i] <= K:
        ans += '1'
        K -= dp[length - i]
    else:
        ans += '0'

print(ans)