import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, q = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    dp = [[[0] * (n+1) for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[0][i][j] = (graph[i-1][j-1], INF)[i != j and graph[i-1][j-1] == 0]
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[k][i][j] = min(dp[k-1][i][j], dp[k-1][i][k] + dp[k-1][k][j])

    ans = []
    for _ in range(q):
        c, s, e = map(int, input().split())

        ans.append(str((-1, dp[c-1][s][e])[dp[c-1][s][e] != INF]))

    return '\n'.join(ans)


if __name__ == "__main__":
    print(main())
