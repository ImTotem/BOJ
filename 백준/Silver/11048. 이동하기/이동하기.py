import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')

def main():
    n, m = map(int, input().split())
    dp = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

    for y in range(1, n + 1):
        for x in range(1, m + 1):
            dp[y][x] += max(dp[y-1][x], dp[y][x-1], dp[y-1][x-1])
    
    return dp[n][m]

if __name__ == "__main__":
    print(main())
