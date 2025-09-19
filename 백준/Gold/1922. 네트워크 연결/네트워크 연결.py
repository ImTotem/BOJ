import sys
input = lambda: sys.stdin.readline().strip()
from heapq import heapify, heappop, heappush

INF = float('inf')

def main():
    n = int(input())
    m = int(input())
    
    ans = 0
    edges = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges[a].append((c, b))
        edges[b].append((c, a))

    sib = []
    visited = 0b11
    pq = edges[1]; heapify(pq)
    while pq:
        c, b = heappop(pq)

        if visited & (1 << b): continue
        sib.append(c)

        visited |= (1 << b)
        ans += c
    
        for e in edges[b]:
            if visited & (1 << e[1]): continue
            heappush(pq, e)

    return ans

if __name__ == "__main__":
    print(main())
