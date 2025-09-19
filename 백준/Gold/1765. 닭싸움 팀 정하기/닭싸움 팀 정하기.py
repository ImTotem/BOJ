import sys
input = lambda: sys.stdin.readline().strip()
from collections import defaultdict

INF = float('inf')

def main():
    n = int(input())
    m = int(input())
    parent = [i for i in range(n + 1)]

    def union(a, b):
        a, b = find(a), find(b)
        if a != b: parent[a] = b
    
    def find(x):
        if x == parent[x]: return x
        parent[x] = find(parent[x])
        return parent[x]
    
    graph = defaultdict(list)

    for _ in range(m):
        o, *args = input().split()
        p, q = map(int, args)

        if o == 'F': union(p, q)
        else:
            graph[p].append(q)
            graph[q].append(p)

    for e in graph:
        for i in range(len(graph[e])-1):
            union(graph[e][i], graph[e][i+1])
    
    return len(set(map(find, parent))) - 1

    
if __name__ == "__main__":
    print(main())
