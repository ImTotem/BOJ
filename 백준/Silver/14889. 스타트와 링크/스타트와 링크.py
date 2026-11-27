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
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]

    ans = inf

    cand = set(range(n))

    size = n >> 1

    for a in icomb(cand, size):
        b = cand - set(a)
        a_total = sum(sum(s[i][j] for j in a) for i in a)
        b_total = sum(sum(s[i][j] for j in b) for i in b)

        ans = min(ans, abs(a_total - b_total))

    return ans

if __name__ == "__main__":
    print(main())
