import sys
input = lambda:sys.stdin.readline().strip()

from heapq import heappop, heappush

def main():
    n = int(input())
    heapq = []

    for _ in range(n):
        heappush(heapq, tuple(map(int, input().split())))

    ans = [heappop(heapq)[1]]
    while heapq:
        s, t = heappop(heapq)

        if ans[0] <= s:
            heappop(ans)
        heappush(ans, t)
    
    return len(ans)
                

print(main())