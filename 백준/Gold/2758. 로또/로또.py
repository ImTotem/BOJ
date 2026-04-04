import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, m = 10, 2000
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1] = [1] * (m + 1)

    for i in range(2, n + 1):
        for j in range(1, m + 1):
            for k in range(1, (j//2) + 1):
                dp[i][j] += dp[i - 1][k]

    for _ in range(int(input())):
        n, m = map(int, input().split())

        print(sum(dp[n][1:m+1]))


if __name__ == "__main__":
    main()
