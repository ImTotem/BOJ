from sys import stdin
import math
input = stdin.readline

N = int(input())
i = 2
if N != 1:
    while N != 1:
        if N % i == 0:
            print(i)
            N=N//i
            continue
        i+=1