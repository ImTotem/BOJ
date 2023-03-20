from sys import stdin
input = stdin.readline

k, n = map(int, input().split())
l = [int(input()) for _ in range(k)]

start, end = 1, max(l)

while start <= end:
    mid = (start + end) // 2

    cnt = sum(i//mid for i in l)
    
    if cnt < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)