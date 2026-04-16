import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())

    dp = [0] * 31
    dp[0] = 1
    dp[2] = 3

    for i in range(4, n + 1):
        dp[i] = dp[i - 2] * 3
        for j in range(4, i + 1, 2):
            dp[i] += dp[i - j] * 2
    
    return dp[n]

if __name__ == "__main__":
    print(main())
