import sys
input = lambda: sys.stdin.readline().strip()
from heapq import heappop, heappush

INF = float('inf')

def main():
    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        a, b, t = map(int, input().split())
        graph[a-1].append((t, b-1))
    
    def dijkstra(x, y):
        pq = [(0, x)]
        visited = [INF] * (n + 1)
        visited[x] = 0
        while pq:
            t, a = heappop(pq)

            if visited[a] < t:
                continue

            for bt, b in graph[a]:
                nt = t + bt

                if visited[b] > nt:
                    heappush(pq, (nt, b))
                    visited[b] = nt
        
        return visited[y]

    return max(dijkstra(x-1, y) + dijkstra(y, x-1) for y in range(n))

    
if __name__ == "__main__":
    print(main())
