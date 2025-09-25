import sys
input = lambda: sys.stdin.readline().strip()
from itertools import accumulate

INF = float('inf')

def main():
    n = int(input())

    MAX = 4_000_000 + 1
    rset = lambda start, end, gap: set(range(start, end, gap))

    prime = rset(5, MAX, 6) | rset(7, MAX, 6)
    prime.add(2)
    prime.add(3)
    
    for i in range(5, int(MAX ** .5) + 1, 6):
        if i in prime:
            prime -= rset(i * i, MAX, i * 6) | rset(i * (i + 2), MAX, i * 6)
        j = i + 2
        if j in prime:
            prime -= rset(j * j, MAX, j * 6) | rset(j * (j + 4), MAX, j * 6)
    
    prime = list(prime)
    prime.sort()
    acc = list(accumulate(prime)) + [0]
    m = len(prime)
    
    ans = 0
    l = -1
    for r in range(m):
        if prime[r] > n: break
        while acc[r] - acc[l] >= n:
            ans += (acc[r] - acc[l] == n)
            l += 1
    
    return ans

if __name__ == "__main__":
    print(main())
