import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    edges.sort(key=lambda x:x[2])

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

    ans = 0
    maxi = 0
    for a, b, c in edges:
        if find(a) == find(b): continue

        union(a, b)

        ans += c
        maxi = max(maxi, c)
        
    return ans - maxi

if __name__ == "__main__":
    print(main())
