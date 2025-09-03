import sys
input = lambda: sys.stdin.readline().strip()
from bisect import bisect_left

INF = float('inf')

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())

    a.sort()
    ans = 0

    for i in range(n):
        j = min(n-1, bisect_left(a, x - a[i]))
        
        if j <= i: break
        if a[i] + a[j] == x: ans += 1
        
    return ans

if __name__ == "__main__":
    print(main())
