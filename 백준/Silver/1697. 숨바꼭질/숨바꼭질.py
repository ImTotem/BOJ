from sys import stdin
input = stdin.readline
from collections import deque

N, K = map(int, input().split())

m = [0 for _ in range(100001)]
m[N] = 0

visited = []
q = deque()
q.append(N)

while q:
    a = q.popleft()
    visited.append(a)

    if a == K:
        print(m[a])
        break

    for i in a-1, a+1, 2*a:
        if 0 <= i <= 100000 and not m[i]:
            q.append(i)
            m[i] = m[a] + 1