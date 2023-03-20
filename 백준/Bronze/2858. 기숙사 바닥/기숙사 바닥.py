import sys

input = lambda: sys.stdin.readline().strip()

r, b = map(int, input().split())

tiles = r+b

divisor = []

for i in range(1, int(tiles**.5)+1):
    if tiles % i == 0:
        divisor.append(i)

for w in divisor:
    l = tiles // w
    if (l+w-2)*2 == r:
        print(l, w)
        break