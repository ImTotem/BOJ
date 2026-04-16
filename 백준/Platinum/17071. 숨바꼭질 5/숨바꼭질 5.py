import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

INF = float('inf')

def main():
    n, k = map(int, input().split())

    MAX = 500_000

    visited = [[0] * (MAX + 1) for _ in range(2)]
    visited[0][n] = 1
    q = deque([(0, n)])
    while q:
        t, x = q.popleft()
        
        y = k + t * (t + 1) // 2

        if y > MAX: break
        if visited[t % 2][y]: return t

        nt = t + 1
        for nx in x-1, x+1, 2*x:
            if not (0 <= nx <= MAX): continue
            if visited[nt % 2][nx]: continue

            q.append((nt, nx))
            visited[nt % 2][nx] = 1
    
    return -1


if __name__ == "__main__":
    print(main())
