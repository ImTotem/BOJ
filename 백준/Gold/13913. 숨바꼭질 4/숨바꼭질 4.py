import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

MAX = 100000

def main():
    n, k = map(int, input().split())

    q = deque()
    q.append(n)
    
    vis = [-1] * (MAX+1)
    vis[n] = n

    while q:
        x = q.popleft()

        if x == k:
            ans = [x]
            while ans[-1] != n:
                ans.append(vis[ans[-1]])

            return ans[::-1]
        
        for y in x-1, x+1, 2*x:
            if 0 <= y <= MAX and vis[y] == -1:
                q.append(y)
                vis[y] = x

ans = main()
print(len(ans)-1)
print(*ans)