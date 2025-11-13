import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')

def main():
    n = int(input())
    dp = list(map(int, input().split()))

    ans = dp[0]
    for i in range(1, n):
        dp[i] = max(dp[i], dp[i] + dp[i-1])
        ans = max(ans, dp[i])
    
    return ans

if __name__ == "__main__":
    print(main())
