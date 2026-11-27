
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

def main():
    n, m, k = map(int, input().split())
    board = [list(input()) for _ in range(n)]

    acc = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            acc[i+1][j+1] = acc[i][j+1] + acc[i+1][j] - acc[i][j] + (board[i][j] != ('B' if (i + j) % 2 == 0 else 'W'))

    ans = k * k

    for i in range(k, n + 1):
        for j in range(k, m + 1):
            cnt = acc[i][j] - acc[i-k][j] - acc[i][j-k] + acc[i-k][j-k]
            ans = min(ans, cnt, k*k - cnt)

    return ans


if __name__ == "__main__":
    print(main())
