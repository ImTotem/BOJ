from itertools import combinations as comb
import sys

input = lambda: sys.stdin.readline().strip()

a = list(comb([int(input()) for _ in range(9)], 7))

for i in a:
    if sum(i) == 100:
        print(*sorted(i), sep="\n")
        break