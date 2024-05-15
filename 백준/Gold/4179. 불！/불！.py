import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

D = [0, 1, 0, -1, 0]

def main():
    r, c = map(int, input().split())
    maze = []
    
    q = deque()
    fire = deque()
    for i in range(r):
        maze.append(list(input()))
        
        for j in range(c):
            if maze[i][j] == 'J':
                q.append((j, i, 0))
                maze[i][j] = '.'
            if maze[i][j] == 'F': fire.append((j, i))
    
    def spread():
        for _ in range(len(fire)):
            x, y = fire.popleft()

            for i in range(4):
                nx, ny = x + D[i], y + D[i+1]

                if 0 <= nx < c and 0 <= ny < r and maze[ny][nx] == '.':
                    fire.append((nx, ny))
                    maze[ny][nx] = 'F'

    visited = [[False] * c for _ in range(r)]
    visited[q[0][1]][q[0][0]] = True

    pcnt = -1
    while q:
        x, y, cnt = q.popleft()

        if cnt != pcnt:
            pcnt = cnt
            spread()

        if x in {0, c-1} or y in {0, r-1}:
            return cnt + 1

        for i in range(4):
            nx, ny, ncnt = x + D[i], y + D[i+1], cnt + 1

            if 0 <= nx < c and 0 <= ny < r and maze[ny][nx] == '.' and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny, ncnt))

        
    return "IMPOSSIBLE"
    

print(main())