import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    cost = [[-1] * 3] + [list(map(int, input().split())) for _ in range(n)]

    ans = float('inf')

    for c in range(3):
        dp = [[-1] * 3 for _ in range(n+1)]

        dp[1] = [float('inf')] * 3
        dp[1][c] = cost[1][c]

        for i in range(2, n+1):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
        dp[n][c] = float('inf')
        ans = min(ans, min(dp[n]))

    return ans

if __name__ == "__main__": 
    print(main())
