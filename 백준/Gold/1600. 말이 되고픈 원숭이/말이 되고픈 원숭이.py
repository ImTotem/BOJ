import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

INF = float('inf')
d = [1, 0, -1, 0, 1, 2, 1, -2, -1, 2, -1, -2, 1]

def main():
    k = int(input())
    w, h = map(int, input().split())
    world = [list(map(int, input().split())) for _ in range(h)]

    q = deque([(0, 0, k, 0)])  # x, y, k, dist
    visited = {(0, 0, k)}
    while q:
        x, y, ck, dist = q.popleft()

        if (x, y) == (w - 1, h - 1):
            return dist

        for i in range(12):
            nx, ny = x + d[i], y + d[i+1]
            nk = max(0, ck - (i > 3))

            if 0 <= nx < w and 0 <= ny < h and world[ny][nx] != 1:
                if ck < 1 and i > 3: continue
                if (nx, ny, nk) in visited: continue
                q.append((nx, ny, nk, dist + 1))
                visited.add((nx, ny, nk))

    return -1
    
if __name__ == "__main__":
    print(main())
