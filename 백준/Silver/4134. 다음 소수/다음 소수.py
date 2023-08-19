import sys
input = lambda:sys.stdin.readline().strip()

from math import sqrt

def is_prime(n):
    if n < 2: return False

    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    
    return True

for _ in range(int(input())):
    n = int(input())

    while True:
        if is_prime(n):
            print(n)
            break
        else:
            n += 1