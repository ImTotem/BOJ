from heapq import *
from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
img = []
img2 = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    line = input().strip()
    img.append(list(line))
    img2.append(list(line.replace('G', 'R')))

graph = [[0 for _ in range(N)] for _ in range(N)]
graph2 = [[0 for _ in range(N)] for _ in range(N)]

def bfs(start, curImg, g):
    color = curImg[start[1]][start[0]]

    if g[start[1]][start[0]] == 0:
        q = deque()
        q.append(start)

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < N and 0 <= ny < N and curImg[ny][nx] == color and g[ny][nx] == 0:
                    q.append([nx, ny])
                    g[ny][nx] = 1
        
        return 1
    
    return 0
    
a, b = 0, 0
for i in range(N):
    for j in range(N):
        a += bfs([j, i], img, graph)
        b += bfs([j, i], img2, graph2)

print(a, b)