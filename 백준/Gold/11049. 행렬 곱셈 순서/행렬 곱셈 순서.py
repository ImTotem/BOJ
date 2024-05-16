import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    mat = tuple(tuple(map(int, input().split())) for _ in range(n))
    
    dp = [[0] * n for _ in range(n)]

    for term in range(1, n):
        for lo in range(n - term):
            dp[lo][hi:=lo + term] = int(1e9)
            for i in range(lo, hi):
                dp[lo][hi] = min(
                    dp[lo][hi],
                    dp[lo][i] + dp[i+1][hi] + mat[lo][0] * mat[i][1] * mat[hi][1]
                )

    return dp[0][-1]

print(main())