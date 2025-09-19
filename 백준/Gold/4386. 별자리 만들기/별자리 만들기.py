import sys
input = lambda: sys.stdin.readline().strip()
from heapq import heapify, heappop, heappush

INF = float('inf')

def main():
    n = int(input())
    stars = [tuple(map(float, input().split())) for _ in range(n)]
    
    edges = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            x1, y1, x2, y2 = *stars[i], *stars[j]
            edges.append((((x1-x2)**2 + (y1-y2)**2)**.5, i, j))
    heapify(edges)

    parent = list(range(n))

    def union(a, b):
        a, b = find(a), find(b)
        if a != b: parent[a] = b
    
    def find(x):
        if x == parent[x]: return x
        parent[x] = find(parent[x])
        return parent[x]

    ans = 0
    while edges and len(set(parent)) != 1:
        c, a, b = heappop(edges)

        if find(a) == find(b): continue

        union(a, b)

        ans += c    
        
    return f'{ans:.2f}'

if __name__ == "__main__":
    print(main())
