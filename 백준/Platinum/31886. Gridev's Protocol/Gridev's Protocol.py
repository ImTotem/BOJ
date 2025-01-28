import sys
input = lambda: sys.stdin.readline().strip()

from collections import deque

def solve(n, m, k, edges, start_with_row):
    r = [set() for _ in range(n+1)]
    c = [set() for _ in range(n+1)]
    
    for a, b in edges:
        r[a].add(b)
        c[b].add(a)
    
    q = deque()
    if start_with_row:
        for i in range(1, n+1):
            if len(r[i]) <= k:
                q.append((0, i))  # row = 0
        for i in range(1, n+1):
            if len(c[i]) <= k:
                q.append((1, i))  # col = 1
    else:
        for i in range(1, n+1):
            if len(c[i]) <= k:
                q.append((1, i))
        for i in range(1, n+1):
            if len(r[i]) <= k:
                q.append((0, i))
    
    removed = 0
    cnt = 0
    before = -1
    
    while q:
        typ, num = q.popleft()
        if typ == 0 and not r[num]: continue
        if typ == 1 and not c[num]: continue
        
        if typ != before:
            cnt += 1
            before = typ
            
        if typ == 0:  # row
            for col in list(r[num]):
                c[col].remove(num)
                removed += 1
                if len(c[col]) <= k:
                    q.append((1, col))
            r[num].clear()
        else:  # column
            for row in list(c[num]):
                r[row].remove(num)
                removed += 1
                if len(r[row]) <= k:
                    q.append((0, row))
            c[num].clear()
    
    return cnt if removed == m else float('inf')

def main():
    n, m, k = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))
    
    ans = min(solve(n, m, k, edges, True), solve(n, m, k, edges, False))
    return -1 if ans == float('inf') else ans

if __name__ == "__main__":
    print(main())
