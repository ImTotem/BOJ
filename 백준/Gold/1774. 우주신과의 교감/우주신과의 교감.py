import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, m = map(int, input().split())
    c = [tuple(map(int, input().split())) for _ in range(n)]
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    def union(a, b):
        a, b = find(a), find(b)
        a, b = (b, a) if rank[a] > rank[b] else (a, b)
        
        parent[a] = b
        rank[b] += 1
    
    def find(x):
        if x == parent[x]: return x
        parent[x] = find(parent[x])
        return parent[x]

    def dist(a, b):
        x1, y1, x2, y2 = *c[a - 1], *c[b - 1]
        return ((x2 - x1)**2 + (y2 - y1)**2)**.5
    
    for a, b in edges:
        if find(a) != find(b):
            union(a, b)
    
    edges = list(set((a, b) for a in range(1, n) for b in range(a + 1, n + 1)) - set(edges))
    edges.sort(key=lambda x:dist(*x))

    ans = 0
    for a, b in edges:
        if find(a) != find(b):
            ans += dist(a, b)
            union(a, b)

    return f'{ans:.2f}'
        

if __name__ == "__main__":
    print(main())
