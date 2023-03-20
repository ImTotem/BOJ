from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

graph = list(range(101))

for _ in range(N):
    x, y = map(int, input().split())
    graph[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    graph[u] = v

q = deque()
q.append(1)

move = [0 for _ in range(101)]

while q:
    u = q.popleft()

    if u == 100:
        print(move[u])
        break

    for i in range(1, 7):
        v = u + i
        if 0 < v < 101:
            v = graph[v]
            if move[v] == 0 and v not in q:
                q.append(v)
                move[v] = move[u] + 1