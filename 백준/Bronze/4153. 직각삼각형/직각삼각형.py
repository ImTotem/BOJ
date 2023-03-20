from sys import stdin
import math
input = stdin.readline

while True:
    a = list(map(int, input().split()))

    if a == [0, 0, 0]:break

    m = max(a)
    a.remove(m)

    if a[0]**2+a[1]**2 == m**2:
        print("right")
    else:
        print("wrong")