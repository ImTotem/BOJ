import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    m = int(input())
    parent = list(range(n + 1))

    graph = tuple(tuple(map(int, input().split())) for _ in range(n))
    plan = tuple(map(int, input().split()))

    def union(a, b):
        a, b = find(a), find(b)
        if a != b: parent[a] = b
    
    def find(a):
        if a == parent[a]: return a
        parent[a] = find(parent[a])
        return parent[a]
    
    for i in range(n-1):
        for j in range(i+1, n):
            if graph[i][j]: union(i+1, j+1)
    
    for i in range(m-1):
        if find(plan[i]) != find(plan[i+1]):
            return 'NO'
    
    return 'YES'

if __name__ == "__main__":
    print(main())

