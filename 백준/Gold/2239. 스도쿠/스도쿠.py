import sys
input = lambda:sys.stdin.readline().strip()

board = [list(map(int, list(input()))) for _ in range(9)]
zero = [(j, i) for i in range(9) for j in range(9) if board[i][j] == 0]

def get(x, y):
    ret = set(range(1, 10))

    ret -= set(board[y])
    ret -= set(board[y][x] for y in range(9))

    seg_x, seg_y = 3*(x//3), 3*(y//3)

    ret -= set(
        board[i][j]
        for i in range(seg_y, seg_y+3)
        for j in range(seg_x, seg_x+3)
    )

    return sorted(ret)

def dfs(idx):
    if len(zero) == idx:
        print(*map(lambda x:''.join(map(str, x)), board), sep="\n")
        exit()
    
    x, y = zero[idx]
    for i in get(x, y):
        board[y][x] = i
        dfs(idx+1)
        board[y][x] = 0

dfs(0)