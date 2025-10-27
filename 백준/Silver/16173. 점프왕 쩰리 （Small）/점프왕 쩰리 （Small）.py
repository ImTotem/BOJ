import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

INF = float('inf')

def main():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1

    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()

        if board[y][x] == - 1:
            return 'HaruHaru'
        
        for d in (1, 0), (0, 1):
            nx, ny = x + (d[0] * board[y][x]), y + (d[1] * board[y][x])

            if not (nx < n and ny < n): continue
            if visited[ny][nx]: continue
            visited[ny][nx] = 1
            q.append((nx, ny))
    
    return 'Hing'

if __name__ == "__main__":
    print(main())
