import sys
input = lambda: sys.stdin.readline().strip()
from math import ceil

INF = float('inf')

def main():
    n = int(input())
    dp = [0] + list(map(int, input().split()))

    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            dp[i] = max(dp[i], dp[j] + dp[i - j])
    
    return dp[n]


if __name__ == "__main__":
    print(main())
