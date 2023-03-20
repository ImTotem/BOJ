from heapq import heappop as pop, heappush as push
INF = float("inf")
from sys import stdin
input = stdin.readline

V, E = map(int, input().split())

K = int(input())

graph = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])

def dijkstra(start):
    pq = []
    visited = [INF] * (V+1)
    push(pq, (0, start))
    visited[start] = 0

    while pq:
        wu, u = pop(pq)

        if visited[u] < wu:
            continue

        for wv, v in graph[u]:
            wuv = wu + wv

            if visited[v] > wuv:
                push(pq, [wuv, v])
                visited[v] = wuv
        
    return visited

visited = dijkstra(K)

for i in range(1, V+1):
    print(["INF", visited[i]][visited[i] != INF])