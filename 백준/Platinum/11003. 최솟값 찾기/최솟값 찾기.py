import sys
input = lambda:sys.stdin.readline().strip()

from heapq import heappop, heappush

def main():
    n, l = map(int, input().split())
    a = list(map(int, input().split()))

    ans = []
    hq = []

    for i in range(n):
        while 0 <= i-l and hq and hq[0][1] < i-l+1: heappop(hq)
        heappush(hq, (a[i], i))
        ans.append(hq[0][0])
    
    print(*ans)

main()
