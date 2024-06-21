import sys
input = lambda:sys.stdin.readline().strip()

def main():
    t, w = map(int, input().split())
    jadu = [int(input()) for _ in range(t)]

    dp = [[0] * (t+1) for _ in range(2)]
    
    for i in range(w+1):
        for j in range(1, t+1):
            dp[1][j] = dp[1][j-1]

            a = jadu[j-1] == i % 2 + 1

            dp[1][j] = max(dp[0][j], max(dp[1][j-1], dp[0][j-1]) + a)

        dp[0] = dp[1][:]

    return dp[-1][-1]

print(main())