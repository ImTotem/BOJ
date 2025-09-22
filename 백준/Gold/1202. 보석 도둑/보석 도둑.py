import sys
input = lambda: sys.stdin.readline().strip()
from heapq import heapify, heappop, heappush

INF = float('inf')

def main():
    n, k = map(int, input().split())
    jewels = [tuple(map(int, input().split())) for _ in range(n)]
    bags = [int(input()) for _ in range(k)]
    jewels.sort(); bags.sort()
    
    ans = 0
    pq = []
    for bag in bags:
        while jewels and jewels[0][0] <= bag:
            heappush(pq, -heappop(jewels)[1])
        
        if pq: ans -= heappop(pq)

    return ans


if __name__ == "__main__":
    print(main())
