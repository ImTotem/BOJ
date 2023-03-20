from sys import stdin
import math
input = stdin.readline

T = int(input())
for _ in range(T):
    H, W, N = list(map(int, input().split()))
    h = N % H
    if h == 0: h = H
    print(int(str(h)+(str(math.ceil(N/H)).zfill(2))))