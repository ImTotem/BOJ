import sys
input = lambda:sys.stdin.readline().strip()

from math import ceil, log2

class Seg:
    def __init__(self, n, a) -> None:
        self.size = 2**ceil(log2(n))
        self.tree = [0] * (2*self.size)
        self.lazy = [0] * (2*self.size)

        for i in range(n): self.tree[self.size+i] = a[i]
        for i in range(self.size-1, 0, -1): self.tree[i] = self.tree[2*i] ^ self.tree[2*i+1]

    def update(self, l, r, x, n=1, nl=0, nr=None):
        if nr == None: nr = self.size - 1
        self.propagate(n, nl, nr)
        if nr < l or r < nl: return
        if l <= nl and nr <= r:
            self.lazy[n] ^= x
            self.propagate(n, nl, nr)
            return
        
        mid = (nl + nr) // 2
        self.update(l, r, x, 2*n, nl, mid)
        self.update(l, r, x, 2*n+1, mid+1, nr)
        self.tree[n] = self.tree[2*n] ^ self.tree[2*n+1]

    def query(self, l, r, n=1, nl=0, nr=None):
        if nr == None: nr = self.size - 1
        self.propagate(n, nl, nr)

        if nr < l or r < nl: return 0
        if l <= nl and nr <= r: return self.tree[n]

        mid = (nl + nr) // 2
        return self.query(l, r, 2*n, nl, mid) ^ self.query(l, r, 2*n+1, mid+1, nr)
    
    def propagate(self, n, nl, nr):
        if self.lazy[n] != 0:
            if n < self.size:
                self.lazy[2*n] ^= self.lazy[n]
                self.lazy[2*n+1] ^= self.lazy[n]
            if self.size <= n: self.tree[n] ^= self.lazy[n]
            self.lazy[n] = 0

def main():
    n = int(input())
    a = list(map(int, input().split()))

    seg = Seg(n, a)
    
    for _ in range(int(input())):
        s, i, *j = map(int, input().split())

        if s == 1: seg.update(i, j[0], j[1])
        else: print(seg.query(i, j[0]))

main()