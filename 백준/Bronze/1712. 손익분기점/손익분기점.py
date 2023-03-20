from sys import stdin
import math
input = stdin.readline

A, B, C = list(map(int, input().split()))

answer = -1

if B < C:
    answer = math.floor(A/(C-B))+1
print(answer)