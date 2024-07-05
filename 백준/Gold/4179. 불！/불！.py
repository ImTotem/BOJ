import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

D = [0, 1, 0, -1, 0]

def main():
    r, c = map(int, input().split())
    maze = [list(input()) for _ in range(r)]

    q = deque()
    fire = deque()

    visited = [[False] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'F':
                fire.append((j, i))
            elif maze[i][j] == 'J':
                maze[i][j] = '.'
                q.append((j, i, 0))

    def spread():
        for _ in range(len(fire)):
            x, y = fire.popleft()

            for i in range(4):
                nx, ny = x + D[i], y + D[i+1]

                if 0 <= nx < c and 0 <= ny < r and maze[ny][nx] == '.':
                    fire.append((nx, ny))
                    maze[ny][nx] = 'F'

    visited[q[0][1]][q[0][0]] = True

    prev = -1
    while q:
        x, y, sec = q.popleft()

        if prev != sec:
            prev = sec
            spread()

        if x in {0, c-1} or y in {0, r-1}:
            return sec + 1

        for i in range(4):
            nx, ny = x + D[i], y + D[i+1]

            if 0 <= nx < c and 0 <= ny < r and maze[ny][nx] == '.' and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny, sec+1))
    
    return "IMPOSSIBLE"

print(main())