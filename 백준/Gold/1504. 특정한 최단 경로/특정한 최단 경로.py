from heapq import heappop as pop, heappush as push
INF = float("inf")
from sys import stdin
input = stdin.readline

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    pq = []
    visited = [INF] * (N+1)
    push(pq, (0, start))
    visited[start] = 0

    while pq:
        cur_cost, cur_node = pop(pq)

        if visited[cur_node] < cur_cost:
            continue

        for next_cost, next_node in graph[cur_node]:
            next_sum_cost = cur_cost + next_cost

            if visited[next_node] > next_sum_cost:
                push(pq, [next_sum_cost, next_node])
                visited[next_node] = next_sum_cost

    return visited[end]

ans = min(
    dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N), 
    dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
    )

print(ans if ans != INF else -1)