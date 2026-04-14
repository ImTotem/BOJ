import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    s = input()
    n = len(s)

    pal = [[0] * n for _ in range(n)]
    
    for i in range(n):
        pal[i][i] = 1

        if i == n - 1: continue

        if s[i] == s[i + 1]:
            pal[i][i + 1] = 1
    
    for i in range(3, n + 1):
        for start in range(n - i + 1):
            end = start + i - 1
            if s[start] == s[end] and pal[start + 1][end - 1]:
                pal[start][end] = 1
    
    dp = [2500] * (n + 1)
    dp[n] = 0
    for j in range(n):
        for i in range(j + 1):
            dp[j] = min(dp[j], dp[(i if pal[i][j] else j) - 1] + 1)

    return dp[n - 1]

if __name__ == "__main__":
    print(main())
