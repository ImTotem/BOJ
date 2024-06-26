import sys
input = lambda:sys.stdin.readline().strip()

from heapq import heappush, heappop

# 크루스칼
def main():
    n, m = map(int, input().split())

    pq, s = [], 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        heappush(pq, (c, a, b))
        s += c

    parent = list(range(n+1))

    def find(x):
        if parent[x] == x: return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    ans, cnt = 0, 0
    while pq:
        c, a, b = heappop(pq)
        
        if find(a) != find(b):
            ans += c
            union(a, b)
            cnt += 1
        
        if cnt == n-1: break
    
    return -1 if cnt != n-1 else s - ans

print(main())