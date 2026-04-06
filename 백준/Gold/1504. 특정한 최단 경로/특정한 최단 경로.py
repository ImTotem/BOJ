import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict
from heapq import heappop, heappush

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    n, e = map(int, input().split())
    graph = defaultdict(set)

    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].add((c, b))
        graph[b].add((c, a))
    
    v1, v2 = map(int, input().split())
    
    def dij(s):
        pq = [(0, s)]
        visited = [INF] * (n + 1)
        visited[s] = 0

        while pq:
            uc, u = heappop(pq)

            if uc > visited[u]: continue

            for vc, v in graph[u]:
                c = uc + vc

                if visited[v] > c:
                    heappush(pq, (c, v))
                    visited[v] = c
        
        return visited

    w1, w2 = dij(v1), dij(v2)
    
    ans = min(
        w1[1] + w1[v2] + w2[n],
        w2[1] + w2[v1] + w1[n]
    )

    return ans if ans != INF else -1
    

if __name__ == "__main__":
    print(main())
