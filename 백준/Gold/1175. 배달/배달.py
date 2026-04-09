import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    n, m = map(int, input().split())
    graph = []
    s = (0, 0)
    
    rep, idx = 'CD', 0
    
    for y in range(n):
        graph.append(list(input()))
        
        for x in range(m):
            if graph[y][x] == 'S':
                s = (x, y)
            elif graph[y][x] == 'C':
                graph[y][x] = rep[idx]
                idx += 1
    
    q = deque([(*s, -1, 0, 0)])
    visited = [[[[0] * 4 for _ in range(4)] for _ in range(m)] for _ in range(n)]

    while q:
        x, y, d, c, t = q.popleft()
        
        if c == 0b11:
            return t

        for i in range(4):
            if i == d: continue
            nx, ny, nc = x + D[i], y + D[i + 1], c
            
            if not (0 <= nx < m and 0 <= ny < n): continue
            if graph[ny][nx] == '#': continue
            
            if graph[ny][nx] == 'C':
                nc |= 0b01
            elif graph[ny][nx] == 'D':
                nc |= 0b10
            
            if not visited[ny][nx][i][nc]:
                visited[ny][nx][i][nc] = 1
                q.append((nx, ny, i, nc, t + 1))
    
    return -1


if __name__ == "__main__":
    print(main())
