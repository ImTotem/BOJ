from sys import stdin
input = stdin.readline


N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

max_dp = dp[0][:]
min_dp = dp[0][:]

for i in range(1, N):
    max_dp = [
        dp[i][0] + max(max_dp[0], max_dp[1]),
        dp[i][1] + max(max_dp),
        dp[i][2] + max(max_dp[1], max_dp[2])
    ]

    min_dp = [
        dp[i][0] + min(min_dp[0], min_dp[1]),
        dp[i][1] + min(min_dp),
        dp[i][2] + min(min_dp[1], min_dp[2])
    ]

print(max(max_dp), min(min_dp))