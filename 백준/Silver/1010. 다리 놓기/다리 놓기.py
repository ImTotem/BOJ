import math, re
from sys import stdin
input = stdin.readline

for i in range(int(input())):
    print(math.comb(*reversed(list(map(int, input().split())))))