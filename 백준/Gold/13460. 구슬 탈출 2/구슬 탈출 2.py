import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

D = [0, 1, 0, -1, 0]

def mv_r(dx, dy):
    nx, ny = rx ,ry
    while board[ny+dy][nx+dx] == '.':
        nx += dx;ny += dy
    
    if goal == (nx+dx, ny+dy): nx += dx; ny += dy
    board[ny][nx] = 'X'
    return nx, ny

def mv_b(dx, dy):
    nx, ny = bx ,by
    while board[ny+dy][nx+dx] == '.':
        nx += dx;ny += dy
    
    if goal == (nx+dx, ny+dy): nx += dx; ny += dy
    board[ny][nx] = 'X'
    return nx, ny

def mv(dx, dy):
    f = [mv_r, mv_b]
    if (dx == -1 and bx < rx)\
    or (dx == 1 and rx < bx)\
    or (dy == -1 and by < ry)\
    or (dy == 1 and ry < by): f = f[::-1]
    
    ret = list(map(lambda x:x(dx, dy), f))
    if f != [mv_r, mv_b]: ret = ret[::-1]

    for pos in ret: board[pos[1]][pos[0]] = ['.', 'O'][goal == pos]

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