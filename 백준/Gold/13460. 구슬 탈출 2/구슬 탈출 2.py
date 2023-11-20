import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

D = [0, 1, 0, -1, 0]

def mv(dx, dy):
    f = [(rx, ry), (bx, by)]
    if (dx == -1 and bx < rx)\
    or (dx == 1 and rx < bx)\
    or (dy == -1 and by < ry)\
    or (dy == 1 and ry < by): f = f[::-1]

    ret = []

    for nx, ny in f:
        while board[ny+dy][nx+dx] == '.':
            nx += dx;ny += dy
        
        if goal == (nx+dx, ny+dy): nx += dx; ny += dy
        board[ny][nx] = 'X'
        ret.append((nx, ny))

    if f != [(rx,ry), (bx,by)]: ret = ret[::-1]

    for x, y in ret: board[y][x] = ['.', 'O'][goal == (x,y)]

    return sum(ret, ())

n, m = map(int, input().split())
board = []

goal = None
rx, ry = 0, 0
bx, by = 0, 0
for i in range(n):
    line = list(input())
    
    for j in range(m):
        if line[j] == 'R':
            rx, ry = j, i
            line[j] = '.'
        elif line[j] == 'B':
            bx, by = j, i
            line[j] = '.'
        elif line[j] == 'O': goal = (j, i)
    board.append(line)

q = deque()
q.append((0, rx, ry, bx, by))
visited = set()
visited.add((rx, ry, bx, by))

ans = -1
while q and q[0][0] < 11:
    cnt, rx, ry, bx, by = q.popleft()
    if goal == (rx, ry):
        ans = cnt
        break

    for i in range(4):
        ps = mv(D[i], D[i+1])

        if ps not in visited and goal != (ps[2], ps[3]):
            q.append((cnt + 1, *ps))
            visited.add(ps)

print(ans)
