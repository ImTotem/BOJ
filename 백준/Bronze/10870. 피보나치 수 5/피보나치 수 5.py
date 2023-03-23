from sys import stdin
import math
input = stdin.readline

n = int(input())
n1 = 0
n2 = 1
n3 = 1
for _ in range(n-2):
    n1 = n2
    n2 = n3
    n3 = n1+n2

if n == 0:
    print(n1)
else: print(n3)