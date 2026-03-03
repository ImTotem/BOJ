import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush

INF = float('inf')

def main():
    n, m = int(input()), int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
    
    a, b = map(int, input().split())

    visited = [INF] * (n + 1)
    visited[a] = 0
    pq = [(0, a)]
    while pq:
        uc, u = heappop(pq)
        
        if visited[u] < uc: continue

        for vc, v in graph[u]:
            uvc = uc + vc

            if visited[v] > uvc:
                heappush(pq, (uvc, v))
                visited[v] = uvc

    return visited[b]

if __name__ == "__main__":
    print(main())
