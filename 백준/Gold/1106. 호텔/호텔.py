import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    c, n = map(int, input().split())
    dp = [[INF] * 2001 for _ in range(21)]
    ans = INF

    for i in range(n + 1):
        dp[i][0] = 0
    
    for i in range(1, n + 1):
        a, b = map(int, input().split())

        for j in range(1100):
            dp[i][j] = dp[i-1][j]

        for j in range(1100):
            dp[i][j + b] = min(dp[i][j + b], dp[i][j] + a)
        
        for j in range(c, 1100):
            ans = min(ans, dp[i][j])
    
    return ans

if __name__ == "__main__":
    print(main())
