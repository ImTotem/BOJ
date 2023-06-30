import sys
input = lambda:sys.stdin.readline().strip()

n, x = map(int, input().split())
a = list(map(int, input().split()))

_min = float('inf')
for i in range(n-1):
    _min = min(_min, a[i] + a[i+1])

print(x * _min)