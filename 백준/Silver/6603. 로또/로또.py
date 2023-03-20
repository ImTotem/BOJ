from itertools import combinations as comb
from sys import stdin
input = stdin.readline

while True:
    case = list(map(int, input().split()))
    k = case[0]

    if k:
        s = case[1:]
        for i in comb(s, 6):
            print(*i)
        print()
    else:
        break