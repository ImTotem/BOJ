import sys
input = lambda:sys.stdin.readline().strip()

from itertools import accumulate

from bisect import bisect_left

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    acc = [0] + list(accumulate(a))

    ans = 0
    for r in range(1, n+1):
        l = bisect_left(acc, acc[r]-m, hi=r)
        ans += acc[r] - acc[l] == m
    
    return ans

if __name__ == "__main__":
    print(main())