from collections import deque
from sys import stdin
input = stdin.readline

def D(n):
    return (2*n) % 10000

def S(n):
    return [9999, n-1][0 < n]

def L(n):
    s = str(n).zfill(4)
    return int(s[1:]+s[:1])

def R(n):
    s = str(n).zfill(4)
    return int(s[-1:]+s[:-1])

in_ = [map(int, input().split()) for _ in range(int(input()))]
for A, B in in_:
    visited = [False for _ in range(10000)]
    q = deque()
    q.append([A, ""])

    while q:
        u, line = q.popleft()

        if u == B:
            print(line)
            break

        for f in D, S, L, R:
            v = f(u)
            if 0 <= v < 10000 and not visited[v]:
                q.append([v, line + f.__name__])
                visited[v] = True