import sys
input = lambda:sys.stdin.readline().strip()

from math import lcm, gcd
a, b = map(int, input().split())
c, d = map(int, input().split())
m = lcm(b, d)
p = (a*(m//b)+c*(m//d))
x = gcd(p, m)
print(p//x, m//x)