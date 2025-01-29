import sys
input = lambda: sys.stdin.readline().strip()

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

def main():
    n = int(input())
    
    xs, ys, zs = [], [], []
    for i in range(n):
        x, y, z = map(int, input().split())
        xs.append((x, i))
        ys.append((y, i))
        zs.append((z, i))
    
    xs.sort()
    ys.sort()
    zs.sort()
    
    es = []
    
    for coords in (xs, ys, zs):
        for i in range(n-1):
            cost = coords[i+1][0] - coords[i][0]
            a, b = coords[i][1], coords[i+1][1]
            es.append((cost, a, b))
    
    es.sort()
    
    parent = list(range(n))
    ans = 0
    for cost, a, b in es:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            ans += cost
    
    return ans

if __name__ == "__main__":
    print(main())
