import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    m = int(input())
    
    ans = 0
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    edges.sort(key=lambda x:x[2])

    parent = list(range(n + 1))

    def union(a, b):
        a, b = find(a), find(b)
        if a != b: parent[a] = b
    
    def find(x):
        if x == parent[x]: return x
        parent[x] = find(parent[x])
        return parent[x]

    for a, b, c in edges:
        if len(set(parent)) == 2: break
        if find(a) == find(b): continue

        union(a, b)

        ans += c    
        
    return ans

if __name__ == "__main__":
    print(main())
