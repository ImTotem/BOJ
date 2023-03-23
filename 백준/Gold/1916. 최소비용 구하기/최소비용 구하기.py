from heapq import *
from sys import stdin
input = stdin.readline

INF = float("inf")

N = int(input())
M = int(input())

info = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, cost = map(int, input().split())
    info[u].append([cost, v])

start, end = map(int, input().split())

def dijkstra(graph, start, end):
    pq = []
    visited = [INF] * (N+1)
    heappush(pq, (0, start))
    visited[start] = 0

    while pq:
        cur_cost, cur_node = heappop(pq)

        if visited[cur_node] < cur_cost:
            continue

        for next_cost, next_node in graph[cur_node]:
            next_sum_cost = cur_cost + next_cost

            if visited[next_node] > next_sum_cost:
                heappush(pq, [next_sum_cost, next_node])
                visited[next_node] = next_sum_cost

    return visited[end]
    
print(dijkstra(info, start, end))