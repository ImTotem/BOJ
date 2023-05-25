from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

N, Q = map(int, input().split())

usado = {n:[] for n in range(1, N+1)}

for _ in range(N-1):
    p, q, r = map(int, input().split())
    usado[p].append((q, r))
    usado[q].append((p, r))

for _ in range(Q):
    ki, vi = map(int, input().split())

    cnt = 0
    visited = [False] * (N+1)
    que = deque()

    visited[vi] = True
    for v, k in usado[vi]:
        que.append((v, k))
        visited[v] = True

    while que:
        v, k = que.popleft()
        if ki <= k:
            cnt += 1
            for nv, nk in usado[v]:
                if not visited[nv]:
                    que.append((nv, min(k, nk)))
                    visited[nv] = True
    
    print(cnt)