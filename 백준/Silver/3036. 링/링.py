import math, re
from sys import stdin
input = stdin.readline

def d(a, b):
    c = 0
    while c != 1:
        c = math.gcd(a, b)
        a//=c
        b//=c
    return f"{a}/{b}"

n = int(input())
ns = list(map(int, input().split()))

for i in range(1, n):
    print(d(ns[0], ns[i]))