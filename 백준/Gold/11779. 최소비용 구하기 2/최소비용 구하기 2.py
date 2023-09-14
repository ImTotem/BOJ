import sys
input = lambda:sys.stdin.readline().strip()

from heapq import heappop, heappush

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, cost = map(int, input().split())

    graph[u].append([cost, v])

start, end = map(int, input().split())

pq = []
visited = [[float("inf"), 0] for _ in range(n+1)]
heappush(pq, (0, start))
visited[start][0] = 0

while pq:
    cur_cost, cur_node = heappop(pq)

    if visited[cur_node][0] < cur_cost:
        continue

    for next_cost, next_node in graph[cur_node]:
        sum_cost = cur_cost + next_cost

        if sum_cost < visited[next_node][0]:
            heappush(pq, (sum_cost, next_node))
            visited[next_node][0] = sum_cost
            visited[next_node][1] = cur_node

ans = [end]
while ans[-1] != start:
    ans.append(visited[ans[-1]][1])
print(visited[end][0], len(ans), sep="\n");
print(*ans[::-1])