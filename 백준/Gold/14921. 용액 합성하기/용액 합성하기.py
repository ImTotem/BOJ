import sys
input = lambda:sys.stdin.readline().strip()

from bisect import bisect_left

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = float('inf')
    for i in range(n):
        x = min(n-1, bisect_left(a, -a[i]))
        for j in range(max(0, x-1), min(x+1, n)):
            if i == j: continue
            ans = min(ans, a[i] + a[j], key=abs)

        if ans == 0: break
    
    return ans

    
print(main())