import math, re
from sys import stdin
input = stdin.readline

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))