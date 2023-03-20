from sys import stdin
import math
input = stdin.readline

answer = 1

N = int(input())
li = list(input().split())
for i in range(N-1):
    if li[i][-1] != li[i+1][0]:
        answer = 0
        break
print(answer)