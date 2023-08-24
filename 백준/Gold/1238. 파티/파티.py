from heapq import heappop, heappush

import sys
input = lambda:sys.stdin.readline().strip()

INF = float('inf')

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((t, v))

def dijkstra(start, end):
    pq = []
    visited = [INF] * (n+1)
    heappush(pq, (0, start))
    visited[start] = 0

    while pq:
        cur_cost, cur_node = heappop(pq)

        if visited[cur_node] < cur_cost:
            continue

        for nxt_cost, nxt_node in graph[cur_node]:
            sum_cost = cur_cost + nxt_cost

            if visited[nxt_node] > sum_cost:
                heappush(pq, (sum_cost, nxt_node))
                visited[nxt_node] = sum_cost
    
    return visited[end]

print(max(dijkstra(i+1, x) + dijkstra(x, i+1) for i in range(n)))
