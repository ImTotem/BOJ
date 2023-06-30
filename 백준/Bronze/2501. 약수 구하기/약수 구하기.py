import sys
input = lambda:sys.stdin.readline().strip()

n, k = map(int, input().split())

cnt = 0
divisor = 0

for i, div in enumerate(range(1, n+1)):
    if n % div == 0:
        cnt += 1
        if cnt == k:
            divisor = div
            break

print(divisor)