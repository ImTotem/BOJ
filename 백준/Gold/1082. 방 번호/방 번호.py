import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    p = list(map(int, input().split()))
    m = int(input())
    
    dp = [-1] * (m + 1)

    for i in range(n-1, -1, -1):
        for j in range(p[i], m + 1):
            dp[j] = max(dp[j], i, dp[j - p[i]] * 10 + i)
    
    return dp[m]

if __name__ == "__main__":
    print(main())
