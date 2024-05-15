import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

D = [0, 1, 0, -1, 0]

def main():
    n, m = map(int, input().split())
    paper = [list(map(int, input().split())) for _ in range(n)]
    
    paint, mx = 0, 0

    def get(x, y):
        size = 0
        q = deque([(x, y)])
        paper[y][x] = 0

        while q:
            x, y = q.popleft()
            size += 1

            for i in range(4):
                nx, ny = x + D[i], y + D[i+1]

                if 0 <= nx < m and 0 <= ny < n and paper[ny][nx]:
                    paper[ny][nx] = 0
                    q.append((nx, ny))
        
        return size
    
    for y in range(n):
        for x in range(m):
            if paper[y][x]:
                size = get(x, y)
                mx = max(mx, size)
                paint += 1

    return paint, mx
    

print(*main(), sep="\n")