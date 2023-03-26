import sys

input = lambda: sys.stdin.readline().strip()

n, c = map(int, input().split())

house = list(sorted(int(input()) for _ in range(n)))

start, end = 1, house[-1] - house[0]

ans = end
if 2 < c:
    while start < end:
        mid = (start + end) // 2

        cnt = 1
        cur = house[0]
        for i in range(n):
            if house[i] - cur >= mid:
                cur = house[i]
                cnt += 1
        
        if cnt >= c:
            ans = mid
            start = mid+1
        else:
            end = mid

print(ans)