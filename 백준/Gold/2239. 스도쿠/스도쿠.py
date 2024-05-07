import sys
input = lambda:sys.stdin.readline().strip()

board = [list(map(int, list(input()))) for _ in range(9)]
zero = [(x, y) for y in range(9) for x in range(9) if board[y][x] == 0]

def get(x, y):
    bit = 0b1111111110
    for i in board[y]:
        bit &= ~(1<<i)
    
    for i in range(9):
        bit &= ~(1<<board[i][x])

    seg_x, seg_y = 3*(x//3), 3*(y//3)

    for i in range(seg_y, seg_y+3):
        for j in range(seg_x, seg_x+3):
            bit &= ~(1<<board[i][j])

    return bit

def dfs(idx):
    if len(zero) == idx:
        print(*map(lambda x:''.join(map(str, x)), board), sep="\n")
        exit()
    
    x, y = zero[idx]
    bit = get(x, y)
    for i in range(1, 10):
        if bit>>i&1:
            board[y][x] = i
            dfs(idx+1)
            board[y][x] = 0

dfs(0)