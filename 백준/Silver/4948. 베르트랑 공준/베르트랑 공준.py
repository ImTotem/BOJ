from sys import stdin
import math
input = stdin.readline

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

while True:
    n = int(input())
    if n == 0: break
    answer = 0
    for i in range(n+1, 2*n+1):
        if isPrime(i):
            answer+=1
    print(answer)
