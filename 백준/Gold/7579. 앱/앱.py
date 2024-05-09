import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())
    am = list(map(int, input().split()))
    ac = list(map(int, input().split()))
    w = sum(ac)

    dp = [[0] * (w+1) for _ in range(n+1)]

    ans = w + 1

    for i in range(1, n+1):
        for j in range(w+1):
            dp[i][j] = dp[i-1][j]
        for j in range(ac[i-1], w+1):
            dp[i][j] = max(am[i-1] + dp[i-1][j-ac[i-1]], dp[i][j])
            if m <= dp[i][j]: ans = min(ans, j)
    
    return ans

print(main())