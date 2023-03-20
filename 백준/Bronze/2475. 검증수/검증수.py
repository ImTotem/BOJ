import math
from sys import stdin
input = stdin.readline

m = map(int, input().split())
print(sum([i**2 for i in m])%10)