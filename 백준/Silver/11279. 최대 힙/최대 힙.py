from sys import stdin
input = stdin.readline
import heapq as heap

N = int(input())

h = []

for _ in range(N):
    n = int(input())

    if n == 0:
        print(heap.heappop(h)[1]) if h else print(0)
    else:
        heap.heappush(h, [-n, n])