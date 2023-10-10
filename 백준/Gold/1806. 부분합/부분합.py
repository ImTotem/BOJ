import sys
input = lambda:sys.stdin.readline().strip()

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0

tmp = arr[0]
ans = float('inf')

while left <= right:
    if s <= tmp:
        ans = min(ans, right - left + 1)
        tmp -= arr[left]
        left += 1
    else:
        right += 1
        if right < n: tmp += arr[right]
        else: break

print([0, ans][ans != float('inf')])