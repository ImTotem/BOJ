import sys
input = lambda: sys.stdin.readline().strip()
from heapq import heappop, heappush

INF = float('inf')

def main():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    graph2 = [[INF]  * n for _ in range(n)]
    
    for i in range(n):
        graph[i][i] = 0
        graph2[i][i] = 0

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1][b-1] = 1
        graph2[b-1][a-1] = 1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                graph2[i][j] = min(graph2[i][j], graph2[i][k] + graph2[k][j])
    
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph2[i][j])

    return sum(1 for i in graph if INF not in set(i))
    
if __name__ == "__main__":
    print(main())
