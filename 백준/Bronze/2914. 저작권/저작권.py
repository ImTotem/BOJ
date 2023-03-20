import math
from sys import stdin
input = stdin.readline

# math.ceil()

a, l = map(int, input().split())

print(a*(l-1)+1)