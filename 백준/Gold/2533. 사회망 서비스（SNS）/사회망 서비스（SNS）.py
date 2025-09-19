import sys
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10**8)

INF = float('inf')

def main():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    dp = [[0, 1] for _ in range(n + 1)]

    visited = [0] * (n + 1)
    def dfs(parent):
        visited[parent] = 1
        
        for child in graph[parent]:
            if visited[child] != 0: continue

            dfs(child)
            dp[parent][0] += dp[child][1]
            dp[parent][1] += min(dp[child])
    
    dfs(1)

    return min(dp[1])
                
if __name__ == "__main__":
    print(main())
