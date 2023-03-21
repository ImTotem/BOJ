from heapq import heappop, heappush, heapify
import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())

bunch = [int(input()) for _ in range(n)]

heapify(bunch)

cnt = 0

for _ in range(n-1):
    cur = heappop(bunch)+heappop(bunch)
    heappush(bunch, cur)

    cnt += cur

print(cnt)