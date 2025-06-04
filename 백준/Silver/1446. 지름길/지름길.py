import sys
input = lambda: sys.stdin.readline().strip()
from collections import defaultdict
from heapq import heappop, heappush

INF = float('inf')

def main():
    n, d = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(n):
        start, end, cost = map(int, input().split())
        if end <= d:
            graph[start].append((cost, end))
    
    for i in range(d):
        graph[i].append((1, i + 1))
        
    dist = [INF] * (d + 1)
    dist[0] = 0

    pq = [(0, 0)]
    while pq:
        ucost, u = heappop(pq)
        
        if ucost > dist[u]:
            continue

        for vcost, v in graph[u]:
            ncost = ucost + vcost
            if ncost < dist[v]:
                dist[v] = ncost
                heappush(pq, (ncost, v))

    return dist[d]

if __name__ == "__main__":
    print(main())
