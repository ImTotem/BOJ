import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

INF = float('inf')
d = [1, 0, 1, 1, -1, 0, -1, -1, 1]

def main():
    n, m = map(int, input().split())
    graph = []
    sharks = set()

    for y in range(n):
        graph.append(list(map(int, input().split())))
        for x in range(m):
            if graph[y][x]:
                sharks.add((x, y))

    def dist(a, b):
        q = deque([(a, b, 0)])
        visited = [[False] * m for _ in range(n)]
        visited[b][a] = True
        
        while q:
            x, y, l = q.popleft()
            
            for i in range(8):
                nx, ny = x + d[i], y + d[i+1]

                if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                    if graph[ny][nx]: return l + 1
                    visited[ny][nx] = True
                    q.append((nx, ny, l + 1))

    return max(dist(a, b) for b in range(n) for a in range(m) if not graph[b][a])
    
if __name__ == "__main__":
    print(main())
