from sys import stdin
input = stdin.readline

s1 = input().strip()
s2 = input().strip()

x, y = len(s1), len(s2)
dp = [[0] * (x+1) for _ in range(y+1)]

for i in range(1, y+1):
    for j in range(1, x+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if s1[j-1] == s2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1

print(dp[y][x])
