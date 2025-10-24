import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

INF = float('inf')
d = [0, 1, 0, -1, 0]

def main():
    n, m, k = map(int, input().split())
    world = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1 << k

    q = deque([(0, 0, k, 1)])  # x, y, k, dist

    while q:
        x, y, ck, dist = q.popleft()
        night = not (dist % 2)

        if (x, y) == (m - 1, n - 1):
            return dist

        for i in range(4):
            nx, ny = x + d[i], y + d[i+1]

            if not (0 <= nx < m and 0 <= ny < n): continue
            if world[ny][nx] and ck == 0: continue
            if world[ny][nx] and night:
                q.append((x, y, ck, dist + 1))
                continue
            if visited[ny][nx] & (1 << (ck - world[ny][nx])): continue
            visited[ny][nx] |= 1 << (ck - world[ny][nx])
            q.append((nx, ny, ck - world[ny][nx], dist + 1))
    
    return -1
    
if __name__ == "__main__":
    print(main())
