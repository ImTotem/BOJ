from sys import stdin
import math
input = stdin.readline

A, B, V = list(map(int, input().split()))
print(math.ceil((V-B)/(A-B)))
