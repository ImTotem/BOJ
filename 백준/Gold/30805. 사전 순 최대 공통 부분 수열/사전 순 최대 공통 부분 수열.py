import sys
input = lambda:sys.stdin.readline().strip()

from heapq import heappush, heappop

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    
    ans = []
    
    x, y = ([[] for _ in range(101)] for _ in range(2))
    for i, v in enumerate(a): heappush(x[v], i)
    for i, v in enumerate(b): heappush(y[v], i)
    
    mx, my = 0, 0
    for i in range(100, 0, -1):
        while x[i] and x[i][0] < mx: heappop(x[i])
        while y[i] and y[i][0] < my: heappop(y[i])

        while len(x[i]) and len(y[i]):    
            mx = heappop(x[i])
            my = heappop(y[i])
            
            ans.append(a[mx])

    print(len(ans))
    if ans: print(*ans)

main()