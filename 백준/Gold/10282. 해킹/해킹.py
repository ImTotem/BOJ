import sys
input = lambda: sys.stdin.readline().strip()
from heapq import heappop, heappush

INF = float('inf')

def main():
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b-1].append((s, a-1))
    
    pq = [(0, c-1)]
    visited = [INF] * n
    visited[c-1] = 0
    while pq:
        t, a = heappop(pq)

        if visited[a] < t:
            continue

        for bt, b in graph[a]:
            nt = t + bt

            if visited[b] > nt:
                heappush(pq, (nt, b))
                visited[b] = nt
    
    return f'{n - visited.count(INF)} {max(i for i in visited if i != INF)}'
    
if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
