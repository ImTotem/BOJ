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
    ans = '-'

    for i in range(n):
        ans = (' ' * (3 ** i)).join([ans, ans])

    return ans

if __name__ == "__main__":
    try:
        while True:
            print(main())
    except:
        ...