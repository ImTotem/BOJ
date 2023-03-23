from collections import deque
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

MAX = 100001

m = [0] * MAX
visited = [False] * MAX

q = deque()
q.append(N)

while q:
    a = q.popleft()

    if a == K:
        print(m[a])
        break

    for i in a-1, a+1, 2*a:
        if 0 <= i < MAX and not visited[i]:
            if i == 2*a:
                q.appendleft(i)
                m[i] = m[a]
            else:
                q.append(i)
                m[i] = m[a] + 1
            visited[i] = True