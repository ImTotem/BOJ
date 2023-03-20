from sys import setrecursionlimit
setrecursionlimit(10**5)
from sys import stdin
input = stdin.readline

n = int(input())

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(n), n-2)