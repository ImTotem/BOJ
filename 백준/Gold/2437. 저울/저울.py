import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
weight = list(sorted(map(int, input().split())))

target = 1

for i in weight:
    if target < i:
        break

    target += i

print(target)