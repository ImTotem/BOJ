from sys import stdin
input = stdin.readline
from itertools import permutations

N, M = map(int, input().split())
n = list(map(int, input().split()))

for i in sorted(set(permutations(n, M))):
    print(*i)