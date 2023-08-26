import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

n, m = map(int, input().split())
graph = []
cheese = set()

for y in range(n):
    graph.append(list(map(int, input().split())))

    for x in range(m):
        if graph[y][x]:
            cheese.add((x, y))

d = [0, 1, 0, -1, 0]

visited = [[False] * m for _ in range(n)]

def air(pos):
    q = deque()
    q.append((pos))
    visited[pos[1]][pos[0]] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+d[i], y+d[i+1]

            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                if graph[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append((nx, ny))

def find():
    global cheese

    rem = set()
    for x, y in cheese:
        cnt = 0
        for i in range(4):
            nx, ny = x+d[i], y+d[i+1]

            if graph[ny][nx] == 0 and visited[ny][nx]:
                cnt += 1
        
        if 1 < cnt:
            rem.add((x, y))
            graph[y][x] = 0

    cheese -= rem
    for i in rem: air(i)

ans = 0
air((0, 0))
while cheese:
    find()
    ans += 1

print(ans)