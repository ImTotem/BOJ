import sys
input = lambda: sys.stdin.readline().strip()
from heapq import heappop, heappush, heapify

INF = float('inf')

def main():
    n = int(input())
    
    ans = []
    hq = list(range(10))
    heapify(hq)
    while hq:
        cur = heappop(hq)
        ans.append(cur)
        
        for i in range(int(str(cur)[0]) + 1, 10):
            heappush(hq, int(str(i) + str(cur)))

    return ans[n] if n < 1023 else -1
    
if __name__ == "__main__":
    print(main())
