import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    def find(v):
        if parent[v] == v: return v
        parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)

        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
            rank[root_u] += 1
        else:
            parent[root_u] = root_v
            rank[root_v] += 1

    n, m = map(int, input().split())
    graph = [tuple(map(int, input().split())) for _ in range(m)]
    graph.sort(key=lambda x:x[2])

    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    ans = []

    for a, b, c in graph:
        if find(a) != find(b):
            ans.append(c)
            union(a, b)
    
    return sum(ans) - ans[-1]

if __name__ == "__main__":
    print(main())
