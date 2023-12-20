import sys
input = lambda:sys.stdin.readline().strip()

class Fixed:
    hx, hy = 0, 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx, self.dy = x-self.hx, y-self.hy
        self.d = abs(self.dx) + abs(self.dy)
    
    def __gt__(self, other):
        return [(a := self.dy*other.dx)>(b := other.dy*self.dx), self.d > other.d][a==b]
    
    def __repr__(self):
        return f"{self.x} {self.y}"

def main():
    n = int(input())
    pos = [tuple(map(int, input().split())) for _ in range(n+1)]
    hx, hy = pos[-1]
    Fixed.hx, Fixed.hy = pos.pop()
    
    q = [[], []]

    for p in pos: q[hx<p[0] or (hx==p[0] and hy < p[1])].append(Fixed(*p))
    
    for i in range(2): q[i].sort()

    for i in q:
        if i: print(*i, sep="\n")

main()