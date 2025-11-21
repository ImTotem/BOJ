import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')

def main():
    n = int(input())
    dp = [float(input()) for _ in range(n)]

    for i in range(1, n):
        dp[i] = max(dp[i], dp[i-1] * dp[i])

    return f"{max(dp):.3f}"

if __name__ == "__main__":
    print(main())
