import sys
input = lambda:sys.stdin.readline().strip()

MOD = 1000000003

def main():
    n = int(input())
    k = int(input())
    
    dp = [[0] * (k+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = (dp[i-1][j] + dp[i-2-(i==n)][j-1]) % MOD

    return dp[n][k] % MOD

print(main())