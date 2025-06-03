import sys
input = lambda: sys.stdin.readline().strip()
from collections import defaultdict, deque

INF = float('inf')

def main():
    n, m, k, x = map(int, input().split())
    graph = defaultdict(set)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].add(b)
    
    dist = [INF] * (n+1)
    dist[x] = 0
    q = deque()
    for u in graph[x]:
        dist[u] = 1
        q.append(u)
    
    while q:
        u = q.popleft()

        for v in graph[u]:
            if dist[v] == INF:
                dist[v] = dist[u] + 1
                q.append(v)

    ans = [str(i) for i in range(1, n+1) if dist[i] == k]
    return '\n'.join(ans) if ans else -1

if __name__ == "__main__":
    print(main())
