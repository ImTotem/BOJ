from heapq import *
from sys import stdin
input = stdin.readline

heap = []
for _ in range(int(input())):
    x = int(input())

    if x:
        heappush(heap, (abs(x), x))
    else:
        print(heappop(heap)[1] if heap else 0)