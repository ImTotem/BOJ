import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, m, r = map(int, input().split())
    t = list(map(int, input().split()))
    
    graph = [[INF] * n for _ in range(n)]
    for i in range(n): graph[i][i] = 0

    for _ in range(r):
        a, b, l = map(int, input().split())
        graph[a - 1][b - 1] = l
        graph[b - 1][a - 1] = l
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    ans = 0
    for i in range(n):
        ans = max(ans, sum(t[j] for j in range(n) if graph[i][j] <= m))

    return ans
        

if __name__ == "__main__":
    print(main())
