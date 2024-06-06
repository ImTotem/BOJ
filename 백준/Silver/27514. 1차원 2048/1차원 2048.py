import sys
input = lambda:sys.stdin.readline().strip()

from heapq import heapify, heappop, heappush

def main():
    n = int(input())
    a = sorted(map(int, input().split()), reverse=True)

    while a[-1] == 0: a.pop()

    heapify(a)
    
    while 1 < len(a):
        l, r = heappop(a), heappop(a)

        heappush(a, 2*l if l==r else r)
    
    return a[0]


print(main())