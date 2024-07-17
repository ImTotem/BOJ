import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

def main():
    D = [0, 1, 0, -1, 0]
    m, n, k = map(int, input().split())

    visited = [[False] * n for _ in range(m)]

    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())

        for y in range(y1, y2):
            for x in range(x1, x2):
                visited[y][x] = True
    
    ans = []

    for a in range(m):
        for b in range(n):
            if visited[a][b]: continue
            q = deque()
            q.append((b, a))
            visited[a][b] = True
            ans.append(0)

            while q:
                x, y = q.popleft()
                ans[-1] += 1

                for i in range(4):
                    nx, ny = x + D[i], y + D[i+1]

                    if 0 <= nx < n and 0 <= ny < m and not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append((nx, ny))

    return ans

ans = main()
print(len(ans))
print(*sorted(ans))