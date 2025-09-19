import sys
input = lambda: sys.stdin.readline().strip()
from heapq import heappop, heappush

INF = float('inf')

def main():
    v, e = map(int, input().split())
    k = int(input())
    graph = [[] for _ in range(v + 1)]
    
    ans = [INF] * (v + 1)
    ans[k] = 0

    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
    
    pq = [(0, k)]
    while pq:
        c, a = heappop(pq)
        
        if ans[a] < c:
            continue

        for bc, b in graph[a]:
            cc = bc + c
            if ans[b] > cc:
                heappush(pq, (cc, b))
                ans[b] = cc
    
    return '\n'.join(str(ans[i]).upper() for i in range(1, v+1))
    
if __name__ == "__main__":
    print(main())
