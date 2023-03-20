from collections import deque
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

m = [0] * 100001
cnt = 0

q = deque()
q.append(N)

ans = float("inf")

while q:
    a = q.popleft()

    if a == K:
        ans = min(ans, m[a])
        cnt += 1
        continue

    for i in a-1, a+1, 2*a:
        if 0 <= i <= 100000 and ( m[i] == m[a] + 1 or not m[i] ):
            m[i] = m[a] + 1
            q.append(i)

print(ans, cnt, sep="\n")