import sys
input = lambda:sys.stdin.readline().strip()

from math import sqrt

ct = [int(input()) for _ in range(int(input()))]

MAX = max(ct)
is_prime = [0, 0] + [1]*(MAX-1)

for i in range(2, int(sqrt(MAX+1))+1):
    if is_prime[i]:
        j = 2
        while MAX >= (n:=i*j):
            is_prime[n] = 0
            j+=1

for n in ct:
    cnt = 0
    for i in range(2, n//2+1):
        if is_prime[i] and is_prime[n-i]:
            cnt += 1
    print(cnt)
