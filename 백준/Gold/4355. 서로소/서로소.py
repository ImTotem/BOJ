from math import sqrt
import sys

input = lambda: sys.stdin.readline().strip()

def euler_phi(n):
    ret = n
    num = n
    notprime = False

    for i in range(2, int(sqrt(n))+1):
        if num % i == 0:
            notprime = True
            ret = ret // i * (i-1)
            while num % i == 0:
                num //= i

    if notprime == False and n != 1:
        ret -= 1
    elif num != 1:
        ret = ret // num * (num-1)
    
    return ret


while True:
    n = int(input())

    if n == 0: break

    if n != 1:
        print(euler_phi(n))
    else:
        print(0)