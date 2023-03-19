from itertools import combinations as comb
from sys import stdin
input = stdin.readline

n, s = map(int, input().split())
N = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in comb(N, i+1):
        if sum(j) == s:
            ans += 1

print(ans)