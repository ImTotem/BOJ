import sys
input = lambda:sys.stdin.readline().strip()

from heapq import heappop, heappush

def main():
    n, k = map(int, input().split())
    gem = [list(map(int, input().split())) for _ in range(n)]
    bags = [int(input()) for _ in range(k)]
    gem.sort();bags.sort()

    ans = 0
    tmp = []
    for bag in bags:
        while gem and gem[0][0] <= bag:
            heappush(tmp, -heappop(gem)[1])
        
        if tmp: ans -= heappop(tmp)

    print(ans)

main()