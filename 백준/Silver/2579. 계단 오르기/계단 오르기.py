import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    s = [int(input()) for _ in range(n)]
    if n == 1: return s[0]

    dp = [s[0], s[0] + s[1]] + [0] * (n - 2)

    for i in range(2, n):
        dp[i] = s[i] + max(dp[i-2], s[i-1] + dp[i-3])

    return dp[-1]
    
if __name__ == "__main__":
    print(main())
