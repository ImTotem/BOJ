import sys
input = lambda: sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10**8)

from math import gcd, lcm, inf, ceil, perm, comb
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from bisect import bisect_left, bisect_right
from functools import cmp_to_key, cache
from itertools import accumulate as iacc, combinations as icomb, permutations as iperm
from string import ascii_lowercase, ascii_uppercase

MOD = 100_000_007
D = [-1, 0, 1, 0, -1, -1, 1, 1, -1]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0: return 1
    if a > 20 or b > 20 or c > 20: return dp(20, 20, 20)
    return dp(a, b, c)

@cache
def dp(a, b, c):
    if a < b and b < c:
        return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    
    return w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

def main():
    while (tmp := input()) != '-1 -1 -1':
        a, b, c = map(int, tmp.split())

        print(f'w({a}, {b}, {c}) = {w(a, b, c)}')


if __name__ == "__main__":
    main()
