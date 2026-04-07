import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    m, n = map(int, input().split())
    maze = [list(map(int, list(input()))) for _ in range(n)]

    pq = [(0, 0, 0)]
    visited = [[INF] * m for _ in range(n)]
    visited[0][0] = 0

    while pq:
        c, x, y = heappop(pq)

        if c > visited[y][x]: continue

        for i in range(4):
            nx, ny = x + D[i], y + D[i + 1]
            if not (0 <= nx < m and 0 <= ny < n): continue
            nc = c + maze[ny][nx]
            
            if nc < visited[ny][nx]:
                heappush(pq, (nc, nx, ny))
                visited[ny][nx] = nc

    return visited[-1][-1]

if __name__ == "__main__":
    print(main())
