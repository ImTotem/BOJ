import math
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
    
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()
