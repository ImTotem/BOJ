import sys
from itertools import accumulate
from bisect import bisect_right

input = lambda: sys.stdin.readline().rstrip()

inf = float('inf')
d = [-1, 0, 1, 0, -1, -1, 1, 1, -1]

def main():
    n = int(input())
    k = list(map(int, input().split()))
    
    acc = [0] + list(accumulate(k[:-1]))
    s = sum(k)
    
    class bit:
        def __init__(self, sz):
            self.t = [0] * (sz + 1)
            
        def add(self, i, v):
            while i < len(self.t):
                self.t[i] += v
                i += i & (-i)
                
        def q(self, i):
            ret = 0
            while i > 0:
                ret += self.t[i]
                i -= i & (-i)
            return ret
            
    u = sorted(list(set(acc)))
    c = {v: i + 1 for i, v in enumerate(u)}
    
    t1 = bit(len(u))
    b = 0
    for v in reversed(acc):
        i = c[v]
        b += t1.q(i - 1)
        t1.add(i, 1)
        
    a = sorted(acc)
    m = [x % s for x in a]
    um = sorted(list(set(m)))
    mc = {v: i + 1 for i, v in enumerate(um)}
    
    t2 = bit(len(um))
    sq, p, ans = 0, 0, 0
    
    for i in range(n):
        tg = a[i] - 1
        
        while p < n and a[p] <= tg:
            qr = a[p] // s
            mr = a[p] % s
            sq += qr
            t2.add(mc[mr], 1)
            p += 1
            
        qi = (a[i] - 1) // s
        mi = (a[i] - 1) % s
        
        im = bisect_right(um, mi)
        cl = t2.q(im)
        cg = p - cl
        
        ans += p * qi - sq - cg
        
    return ans + b

if __name__ == "__main__":
    print(main())
