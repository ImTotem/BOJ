from sys import stdin
import math
input = stdin.readline

T = int(input())
for _ in range(T):
    x, y = list(map(int, input().split()))
    distance = y - x
    max_ = int(math.sqrt(distance))
    if max_ == math.sqrt(distance):
        print(2*max_-1)
    elif math.sqrt(distance) - max_ <= 0.5:
        print(2*max_)
    else:
        print(2*max_+1)