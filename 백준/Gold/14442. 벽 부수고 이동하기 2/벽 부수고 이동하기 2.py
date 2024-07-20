import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

D = [0, 1, 0, -1, 0]

def main():
    n, m, k = map(int, input().split())

    board = [list(map(int, list(input()))) for _ in range(n)]

    q = deque([(0, 0, 1)]) # r, c, cnt

    visited = [[k+1] * m for _ in range(n)]
    visited[0][0] = 0

    while q:
        r, c, cnt = q.popleft()

        if (r, c) == (n-1, m-1):
            return cnt
        
        for i in range(4):
            nr, nc = r + D[i], c + D[i+1]
            
            if 0 <= nr < n and 0 <= nc < m:
                
                broke = board[nr][nc] + visited[r][c]
                if broke < visited[nr][nc]:
                    visited[nr][nc] = broke
                    q.append((nr, nc, cnt+1))

    return -1

if __name__ == "__main__":
    print(main())