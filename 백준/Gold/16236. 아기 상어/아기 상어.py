from collections import deque
from sys import stdin
input = stdin.readline

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

playerLoc = []
expsLoc = []

for y in range(N):
    for x in range(N):
        if board[y][x] == 9:
            playerLoc = [x, y]
            board[y][x] = 0
        elif board[y][x] > 0:
            expsLoc.append([x, y])

lvl = 2
exp = 0

def path(start, end):
    graph = [[0 for _ in range(N)] for _ in range(N)]

    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()

        if [x, y] == end:
            return graph[y][x]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] == 0 and board[ny][nx] <= lvl:
                q.append([nx, ny])
                graph[ny][nx] = graph[y][x] + 1

    return 0

def filtering():
    return list(filter(lambda x:0 < board[x[1]][x[0]] < lvl, expsLoc))

def getMinPath(times):
    li = sorted(times, key=lambda x:(x[0], x[1][1], x[1][0]))
    for i in li:
        if i[0]:
            return i
    return []

exps = filtering()

sec = 0

while exps:
    times = [[path(playerLoc, i), i] for i in exps]

    mini = getMinPath(times)
    if mini:
        time, expLoc = getMinPath(times)

        x, y = expLoc

        sec += time
        playerLoc = expLoc
        board[y][x] = 0

        if exp + 1 == lvl:
            exp = 0
            lvl += 1
        else:
            exp += 1

        exps = filtering()
    else:
        break

print(sec)