from bisect import bisect_left
import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
a = tuple(sorted(map(int, input().split())))

m = int(input())
for i in map(int, input().split()):
    idx = bisect_left(a, i)
    if idx == n: print(0)
    else: print(int(a[idx] == i))