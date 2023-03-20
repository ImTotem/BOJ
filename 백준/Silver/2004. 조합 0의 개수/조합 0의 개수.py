import math, re
from sys import stdin
input = stdin.readline

def d(a, b):
    c = 0
    while a!=0:
        a//=b
        c+=a
    return c

n, m = map(int, input().split())

two = d(n, 2) - d(m, 2) - d(n-m, 2)
five = d(n, 5) - d(m, 5) - d(n-m, 5)

print(min(two, five))