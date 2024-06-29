import sys
input = lambda:sys.stdin.readline().strip()

from collections import defaultdict

def main():
    n, m = map(int, input().split())
    graph = defaultdict(set)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
    
    def dfs(x):
        vis[x] = True
        s.add(x)
        if len(s) == 5: return 1
        
        for i in graph[x]:
            if vis[i]: continue
            if dfs(i): return 1
            s.discard(i)
            vis[i] = False
        
        return 0

    for i in range(n):
        s, vis = set(), [False] * n
        if dfs(i): return 1

    return 0

print(main())