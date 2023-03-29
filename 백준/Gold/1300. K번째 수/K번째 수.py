import sys

input = lambda: sys.stdin.readline().strip()

n, k = int(input()), int(input())

start, end = 0, k

while start <= end:
    mid = (start + end) // 2
    
    tmp = 0
    for i in range(1, n+1):
        tmp += min(mid//i, n)
    
    if tmp >= k:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print(ans)