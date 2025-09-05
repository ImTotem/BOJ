import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

INF = float('inf')

class P:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h
        self.sub = 0
    
    def fetch(self):
        self.h = max(self.h - self.sub, 0)
        self.sub = 0
        return self.h <= 0
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, o):
        return self.x == o.x and self.y == o.y
    
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.h})"

def main():
    n, m = map(int, input().split())
    s = []
    ibs = set()

    for y in range(n):
        tmp = list(map(int, input().split()))
        for x in range(m):
            tmp[x] = P(x, y, tmp[x])
            if tmp[x].h: ibs.add(tmp[x])        
        s.append(tmp)

    d = [0, 1, 0, -1, 0]
    
    def cnt():
        q = deque()
        visited = set()
        
        ret = 0
        for ib in ibs:
            if ib in visited: continue

            ret += 1
            visited.add(ib)
            q.append(ib)
            while q:
                a = q.popleft()
                
                for i in range(4):
                    nx, ny = a.x + d[i], a.y + d[i+1]
                    
                    if 0 <= nx < m and 0 <= ny < n:
                        if s[ny][nx] in visited: continue
                        if s[ny][nx].h <= 0: continue
                        visited.add(s[ny][nx])
                        q.append(s[ny][nx])
            
        return ret

    ans = 0
    while ibs:
        if cnt() > 1: return ans

        for ib in ibs:
            for i in range(4):
                nx, ny = ib.x + d[i], ib.y + d[i+1]
                ib.sub += bool(0 <= nx < m and 0 <= ny < n and not s[ny][nx].h)
        
        rem = set(ib for ib in ibs if ib.fetch())
        ibs -= rem

        ans += 1

    return 0
    
if __name__ == "__main__":
    print(main())
