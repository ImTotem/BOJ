from sys import stdin
input = stdin.readline
from math import factorial as f

n = int(input())

ans = 0

for i in range(0, n+1, 2):
    a = n - i
    b = i // 2

    ans+=f(a+b)//(f(a)*f(b))

print(ans%10007)