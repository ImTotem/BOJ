from sys import stdin
from collections import deque
input = stdin.readline

c = int(input())
network = [[] for _ in range(c+1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited = []
q = deque()

q.append(1)
while q:
    cur = q.popleft()
    visited.append(cur)
    for i in network[cur]:
        if i not in visited and i not in q:
            q.append(i)

print(len(visited)-1)