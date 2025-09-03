import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

INF = float('inf')

def main():
    f, s, g, u, d = map(int, input().split())
    d = -d

    visited = set()
    q = deque([(s, 0)])
    while q:
        s, cnt = q.popleft()

        if s == g: return cnt

        for i in u, d:
            ns = s + i

            if 1 <= ns <= f and ns not in visited:
                visited.add(ns)
                q.append((ns, cnt + 1))

    return "use the stairs"
    

if __name__ == "__main__":
    print(main())
