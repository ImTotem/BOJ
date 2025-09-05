import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque, defaultdict

INF = float('inf')

def main():
    n = int(input())
    islands = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    outlines = defaultdict(set)

    d = [0, 1, 0, -1, 0]

    tag = 1
    q = deque()
    for y in range(n):
        for x in range(n):
            if not islands[y][x]: continue
            if visited[y][x]: continue

            q.append((x, y))
            while q:
                x, y = q.popleft()

                visited[y][x] = True

                for i in range(4):
                    nx, ny = x + d[i], y + d[i+1]

                    if 0 <= nx < n and 0 <= ny < n:
                        if not islands[ny][nx]: outlines[tag].add((x, y))
                        elif not visited[ny][nx]:
                            q.append((nx, ny))
                            visited[ny][nx] = True
                
            tag += 1
    
    def dist(s, e):
        return min(abs(sx-ex)+abs(sy-ey)-1 for sx, sy in outlines[s] for ex, ey in outlines[e])

    ans = INF
    for i in range(1, tag - 1):
        for j in range(i + 1, tag):
            ans = min(ans, dist(i, j))

    return ans
    
if __name__ == "__main__":
    print(main())
