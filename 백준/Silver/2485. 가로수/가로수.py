from math import gcd
from sys import stdin
input = stdin.readline

n = int(input())
tree = [int(input()) for _ in range(n)]

d = [tree[i+1]-tree[i] for i in range(n-1)]

if d:
    t = gcd(*list(set(d)))
    print(sum(list(map(lambda x:x//t-1, d))))
else:
    print(0)