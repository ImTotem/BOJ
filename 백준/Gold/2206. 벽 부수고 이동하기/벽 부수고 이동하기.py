import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

INF = float('inf')
d = [1, 0, -1, 0, 1]

def main():
    n, m = map(int, input().split())
    world = [list(map(int, list(input()))) for _ in range(n)]

    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True
    
    q = deque([(0, 0, 1, 0)])

    while q:
        x, y, dist, flag = q.popleft()

        if (x, y) == (m-1, n-1):
            return dist

        for i in range(4):
            nx, ny = x + d[i], y + d[i+1]

            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx][flag]:
                if flag and world[ny][nx]: continue
                nflag = flag or world[ny][nx]
                q.append((nx, ny, dist + 1, nflag))
                visited[ny][nx][nflag] = True

    return -1
    
    
if __name__ == "__main__":
    print(main())
