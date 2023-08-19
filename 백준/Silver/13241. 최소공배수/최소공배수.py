import sys
input = lambda:sys.stdin.readline().strip()

from math import lcm
print(lcm(*map(int, input().split())))