import math, re
from sys import stdin
input = stdin.readline

for i in range(int(input())):
    a,b = map(int,input().split())
    print(math.lcm(a, b))