import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heapify, heappop, heappush

INF = float('inf')

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    heapify(a)

    for _ in range(m):
        x, y = heappop(a), heappop(a)
        new = x + y
        heappush(a, new)
        heappush(a, new)
    
    return sum(a)

if __name__ == "__main__":
    print(main())
