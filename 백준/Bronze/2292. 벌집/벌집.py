from sys import stdin
import math
input = stdin.readline

N = int(input())
start = 1

i = 1
while not N <= start:
    start += (6*i)
    i += 1

print(i)