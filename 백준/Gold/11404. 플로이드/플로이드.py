import sys
input = lambda: sys.stdin.readline().strip()
from heapq import heappop, heappush

INF = float('inf')

def main():
    n = int(input())
    m = int(input())

    graph = [[INF] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a-1][b-1] = min(graph[a-1][b-1], c)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    return '\n'.join(' '.join(map(lambda x:str([x, 0][x==INF]), i)) for i in graph)
    
if __name__ == "__main__":
    print(main())
