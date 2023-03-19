import sys

input = lambda: sys.stdin.readline().strip()

minN, maxN = map(int, input().split())

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

print(squareNoNo(maxN) - squareNoNo(minN - 1))