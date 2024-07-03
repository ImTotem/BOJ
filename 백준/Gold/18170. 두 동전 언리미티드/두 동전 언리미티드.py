import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

D = [0, 1, 0, -1, 0]

def main():
    n, m = map(int, input().split())
    board = []
    coins = []

    for i in range(n):
        board.append(list(input()))
        
        for j in range(m):
            if board[i][j] == 'o':
                coins.extend([j, i])
                board[i][j] = '.'
    
    q = deque()
    q.append(coins + [0])
    vis = [[[False] * m for _ in range(n)] for __ in range(2)]
    
    while q:
        x1, y1, x2, y2, cnt = q.popleft()

        if 0 <= x1 < m and 0 <= y1 < n:
            vis[0][y1][x1] = True
            
        if 0 <= x2 < m and 0 <= y2 < n:
            vis[1][y2][x2] = True

        if not (0 <= x1 < m and 0 <= y1 < n)\
        or not (0 <= x2 < m and 0 <= y2 < n):
            return cnt
        
        for i in range(4):
            nx1, ny1 = x1 + D[i], y1 + D[i+1]
            nx2, ny2 = x2 + D[i], y2 + D[i+1]
            
            if not (0 <= nx1 < m and 0 <= ny1 < n)\
            and not (0 <= nx2 < m and 0 <= ny2 < n):
                continue
            
            out1 = False
            vis1 = False
            if 0 <= nx1 < m and 0 <= ny1 < n:
                if board[ny1][nx1] == '#':
                    nx1, ny1 = x1, y1
                vis1 = vis[0][ny1][nx1]
            else: out1 = True
            
            out2 = False
            vis2 = False
            if 0 <= nx2 < m and 0 <= ny2 < n:
                if board[ny2][nx2] == '#':
                    nx2, ny2 = x2, y2
                vis2 = vis[1][ny2][nx2]
            else: out2 = True

            if out1 and out2: continue
            
            if vis1 and vis2: continue

            q.append([nx1, ny1, nx2, ny2, cnt+1])
    
    return -1

print(main())