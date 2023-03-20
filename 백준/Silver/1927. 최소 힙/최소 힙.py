from sys import stdin
input = stdin.readline
import heapq as heap

N = int(input())

h = []

for _ in range(N):
    in_ = int(input())

    if in_ == 0:
        print(heap.heappop(h)) if h else print(0)
    else:
        heap.heappush(h, in_)