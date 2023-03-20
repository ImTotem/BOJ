import sys

input = lambda: sys.stdin.readline().strip()

anses = []

while True:
    n, *h = map(int, input().split())
    h.append(0)
    if n == 0: break

    stack = []
    ans = 0

    for i, cur in enumerate(h):
        while stack and h[stack[-1]] > cur:
            ih = h[stack.pop()]
            
            w = i - stack[-1]-1 if stack else i

            ans = max(ans, w * ih)
            
        stack.append(i)
    
    anses.append(ans)

print(*anses, sep="\n")