import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')

def main():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    dp = [[-1] * (1 << n) for _ in range(n)]

    def dfs(x, visited):
        if dp[x][visited] != -1: return dp[x][visited]

        if visited == (1 << n) - 1:
            if graph[x][0]: return graph[x][0]
            else: return INF

        for i in range(1, n):
            if not graph[x][i]: continue
            if visited & (1 << i): continue

            dp[x][visited] = min(
                dp[x][visited] if dp[x][visited] != -1 else INF,
                dfs(i, visited | (1 << i)) + graph[x][i]
            )
        
        return dp[x][visited] if dp[x][visited] != -1 else INF

    return dfs(0, 1)

if __name__ == "__main__":
    print(main())
