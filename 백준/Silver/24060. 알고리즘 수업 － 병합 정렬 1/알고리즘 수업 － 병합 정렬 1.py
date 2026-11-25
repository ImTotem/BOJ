import sys
input = lambda: sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10**8)

from math import gcd, lcm, inf, ceil, perm, comb
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from bisect import bisect_left, bisect_right
from functools import cmp_to_key
from itertools import accumulate as iacc, combinations as icomb, permutations as iperm
from string import ascii_lowercase, ascii_uppercase

MOD = 100_000_007
D = [-1, 0, 1, 0, -1, -1, 1, 1, -1]


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = -1

    def merge(a, p, q, r):
        nonlocal k, ans
        i, j = p, q + 1
        tmp = []

        while i <= q and j <= r:
            if a[i] <= a[j]:
                tmp.append(a[i])
                i += 1
            else:
                tmp.append(a[j])
                j += 1

        tmp.extend(a[i:q + 1])
        tmp.extend(a[j:r + 1])

        for i, v in enumerate(tmp, p):
            a[i] = v
            k -= 1
            if k == 0: ans = v

    def merge_sort(a, p, r):
        if p >= r: return

        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)

    merge_sort(a, 0, n - 1)
    return ans


if __name__ == "__main__":
    print(main())