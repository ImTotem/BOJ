import sys

input = lambda: sys.stdin.readline().strip()

N = int(input())

ans = [0] * 10

start = 1
d = 1

def calc(a, b):
    while a > 0:
        ans[a%10] += b
        a //= 10

while start <= N:
    while N % 10 != 9:
        calc(N, d)
        N -= 1
    
    if N < start:
        break

    while start % 10 != 0:
        calc(start, d)
        start += 1
    start //= 10
    N //= 10

    for i in range(10):
        ans[i] += (N - start + 1) * d
    d *= 10

print(*ans)