import sys

input = lambda: sys.stdin.readline().strip()

K = int(input())

µ = [0] * 1000001

µ[1] = 1
for i in range(1, 1000001):
    for j in range(2*i, 1000001, i):
        µ[j] -= µ[i]

def squareNoNo(n):
    cnt = 0
    for i in range(1, int(n**0.5)+1):
        cnt += µ[i] * (n // (i*i))
    
    return cnt

l, r = 0, 1000000000000

while l < r - 1:
    mid = ( l + r ) // 2
    if squareNoNo(mid) < K:
        l = mid
    else:
        r = mid

print(r)