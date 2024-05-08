import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    in_degree = [0] * (n+1)
    for _ in range(m):
        s, *order = list(map(int, input().split()))
        for i in range(s-1):
            graph[order[i]].append(order[i+1])
            in_degree[order[i+1]] += 1
    
    ans = []
    q = deque(i for i in range(1, n+1) if in_degree[i] == 0)
    
    for i in range(1, n+1):
        if not q: return [0]
        
        u = q.popleft()
        ans.append(u)

        for j in range(len(graph[u])):
            v = graph[u][j]
            in_degree[v] -= 1
            if (in_degree[v] == 0): q.append(v)
    
    return ans


print(*main(), sep="\n")