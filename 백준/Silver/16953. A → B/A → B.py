from collections import deque
from sys import stdin
input = stdin.readline

A, B = map(int, input().split())

q = deque()
q.append([A, 1])

ans = -1
while q:
    n, cnt = q.popleft()
    
    if n == B:
        ans = cnt
        break

    for i in 2*n, 10*n+1:
        if i <= B and i:
            q.append([i, cnt+1])

print(ans)