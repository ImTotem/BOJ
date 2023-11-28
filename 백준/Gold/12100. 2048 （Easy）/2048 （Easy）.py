import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

def mv(cboard, d):
    board = [[] for _ in range(n)]
    
    if d < 2:
        for y in range(n):
            merged = []
            for x in range(*[(n,), (n-1, -1, -1)][d]):
                if cboard[y][x]:
                    if board[y] and board[y][-1] == cboard[y][x] and not merged[-1]:
                        board[y][-1] *= 2
                        merged[-1] = True
                    else:
                        board[y].append(cboard[y][x])
                        merged.append(False)
            for _ in range(n-len(board[y])): board[y].append(0)
            if d == 1: board[y] = board[y][::-1]
    else:
        for x in range(n):
            tmp = []
            merged = []
            for y in range(*[(n,), (n-1, -1, -1)][d%2]):
                if cboard[y][x]:
                    if tmp and tmp[-1] == cboard[y][x] and not merged[-1]:
                        tmp[-1] *= 2
                        merged[-1] = True
                    else:
                        tmp.append(cboard[y][x])
                        merged.append(False)

            for _ in range(n-len(tmp)): tmp.append(0)
            if d%2: tmp=tmp[::-1]
            for y in range(n): board[y].append(tmp[y])

    return tuple(map(tuple, board))

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ans = max(sum(board, []))

q = deque()
q.append((0, board))
visited = {tuple(map(tuple, board))}

while q and q[0][0] < 6:
    cnt, cboard = q.popleft()
    
    cboard = list(map(list, cboard))
    ans = max(ans, max(sum(cboard, [])))

    for i in range(4):
        nboard = mv(cboard, i)
        if not nboard in visited:
            q.append((cnt+1, nboard))
            visited.add(nboard)

print(ans)