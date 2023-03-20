import sys
from math import ceil

input = lambda: sys.stdin.readline().strip()

print("long "*ceil(int(input())/4) + "int")