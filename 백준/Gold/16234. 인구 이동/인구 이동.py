import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    n, l, r = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    def find(x, y):
        union = {(x, y)}
        q = deque([(x, y)])
        p = graph[y][x]
        
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + D[i], y + D[i + 1]
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in union:
                    if l <= abs(graph[y][x] - graph[ny][nx]) <= r:
                        union.add((nx, ny))
                        q.append((nx, ny))
                        p += graph[ny][nx]
        
        return union, p

    def moved():
        visited = [[0] * n for _ in range(n)]
        unions = []

        for y in range(n):
            for x in range(n):
                if visited[y][x]: continue

                union, p = find(x, y)
                visited[y][x] = 1

                if len(union) < 2: continue
                unions.append((union, p))
        
        if not unions: return False

        for union, p in unions:
            avg = p // len(union)
            for x, y in union:
                graph[y][x] = avg
        
        return True

    t = 0
    while moved():
        t += 1

    return t


if __name__ == "__main__":
    print(main())
