from sys import stdin
import math
input = stdin.readline

M = int(input())
N = int(input())

answer = 0
min_ = 10000

for i in range(M, N+1):
    isPrime = True
    if i == 1:
        isPrime = False
        continue
    for j in range(2, i):
        if i%j == 0:
            isPrime = False
            break
    if isPrime:
        answer += i
        if i < min_:
            min_ = i

if answer==0:
    print(-1)
else:
    print(answer)
    print(min_)