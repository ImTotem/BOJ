from sys import stdin
import math
input = stdin.readline

N = int(input())
ns = list(map(int, input().split()))

answer = 0

for i in ns:
    isPrime = True
    if i == 1:
        isPrime = False
        continue
    for j in range(2, i):
        if i%j == 0:
            isPrime = False
            break
    if isPrime:
        answer += 1

print(answer)