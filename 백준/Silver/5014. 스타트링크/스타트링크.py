import sys
input = lambda: sys.stdin.readline().strip()

from collections import deque

INF = float('inf')

def main():
    f, s, g, u, d = map(int, input().split())
    d = -d

    visited = [0] * (f + 1)
    visited[s] = 1
    q = deque([(s, 0)])

    while q:
        x, cnt = q.popleft()

        if x == g: return cnt

        for m in u, d:
            nx = x + m
            if not (0 < nx <= f): continue
            if visited[nx]: continue
            q.append((nx, cnt + 1))
            visited[nx] = 1

    return 'use the stairs'

if __name__ == "__main__":
    print(main())
