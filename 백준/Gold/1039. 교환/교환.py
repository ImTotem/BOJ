import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    n, k = input().split()
    k = int(k)

    ans = '-1'
    
    visited = {(n, 0)}
    q = deque([(n, 0)])
    while q:
        a, t = q.popleft()

        if t == k:
            ans = max(ans, a)
            continue
            
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                nxt = a[:i]+a[j]+a[i+1:j]+a[i]+a[j+1:]
                if nxt[0] == '0': continue
                if (nxt, t + 1) in visited: continue
                
                visited.add((nxt, t + 1))
                q.append((nxt, t + 1))

    return ans


if __name__ == "__main__":
    print(main())
