import sys
input = lambda: sys.stdin.readline().strip()
from itertools import accumulate as acc
from collections import defaultdict

INF = float('inf')

def main():
    t = int(input())
    n = int(input())
    a = [0] + list(map(int, input().split()))
    m = int(input())
    b = [0] + list(map(int, input().split()))

    a = list(acc(a))
    b = list(acc(b))

    da = defaultdict(int)
    for i in range(n):
        for j in range(i+1, n+1):
            da[a[j] - a[i]] += 1

    ans = 0
    for i in range(m):
        for j in range(i+1, m+1):
            ans += da[t - (b[j] - b[i])]

    return ans

if __name__ == "__main__":
    print(main())
