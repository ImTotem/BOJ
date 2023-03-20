from sys import stdin, setrecursionlimit
input = stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

empty = [[x, y] for y in range(9) for x in range(9) if not board[y][x]]

def bt(idx):
    if len(empty) == idx:
        for i in board:
            print(*i)
        exit(0)

    x, y = empty[idx]

    v1 = [i for i in range(1, 10) if i not in board[y]]

    v2 = [board[i][x] for i in range(9)]
    v2 = [i for i in range(1, 10) if i not in v2]

    xs = x//3*3
    ys = y//3*3
    v3 = sum([board[i][xs:xs+3] for i in range(ys, ys+3)], [])
    v3 = [i for i in range(1, 10) if i not in v3]

    v = [i for i in range(1, 10) if i in v1 and i in v2 and i in v3]
    
    for i in v:
        board[y][x] = i
        bt(idx+1)
        board[y][x] = 0

bt(0)