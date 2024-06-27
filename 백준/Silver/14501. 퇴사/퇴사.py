import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    dp = [0] * (21)
    
    for i in range(1, n+1):
        t, p = map(int, input().split())
        dp[i+t-1] = max(dp[i+t-1], dp[i-1] + p)
        dp[i] = max(dp[i], dp[i-1])

    return dp[n]


print(main())