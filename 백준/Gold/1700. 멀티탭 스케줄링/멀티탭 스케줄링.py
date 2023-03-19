from collections import deque
import sys

input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())
name = deque(map(int, input().split()))

multi_tap = set()

cnt = 0
while name:
    item = name.popleft()
    k -= 1

    if len(multi_tap) == n and item not in multi_tap:
        multi_tap.remove(sorted(multi_tap, key=lambda x:(k - name.index(x) if x in name else 0, name.count(x)))[0])
        cnt += 1

    multi_tap.add(item)

print(cnt)