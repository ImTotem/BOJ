import sys
input = lambda:sys.stdin.readline().strip()

from heapq import heappush, heappop

def main():
    n = int(input())

    ans = []

    for _ in range(n):
        for i in map(int, input().split()):
            heappush(ans, i)
            if len(ans) > n:
                heappop(ans)
    
    
    return ans[0]
    
print(main())