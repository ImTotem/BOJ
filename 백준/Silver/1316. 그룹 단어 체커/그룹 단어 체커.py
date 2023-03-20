from sys import stdin
import math
input = stdin.readline

l = []
N = int(input())
for i in range(N):
    l.append(input())

answer = N
for i in l:
    li = []
    for j in range(len(i)):
        if i[j] in i[:j]:
            if i[j] != i[j-1]:
                answer-=1
                break
print(answer)