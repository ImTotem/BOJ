from sys import stdin
input = stdin.readline
from math import lcm

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    
    ans = -1
    for i in range(x, M*N+1, M):
        if i % N == y % N:
            ans = i
            break
    print(ans)