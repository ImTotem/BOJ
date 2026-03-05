import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush
from collections import deque

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b, d = map(int, input().split())
        d *= 2

        if len({a, b} & {g, h}) == 2:
            d -= 1

        graph[a].append((d, b))
        graph[b].append((d, a))
    
    cs = [int(input()) for _ in range(t)]
    
    visited = [INF] * (n + 1)
    pq = [(0, s)]
    while pq:
        da, a = heappop(pq)

        if da > visited[a]: continue

        for db, b in graph[a]:
            d = da + db

            if d < visited[b]:
                heappush(pq, (d, b))
                visited[b] = d
    
    ans = []
    for c in cs:
        if visited[c] != INF and visited[c] % 2:
            ans.append(c)
    
    ans.sort()
    return ' '.join(map(str, ans))

if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
