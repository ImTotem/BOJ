import sys
input = lambda: sys.stdin.readline().strip()

from collections import deque

INF = float('inf')

def main():
    n = int(input())
    q = deque(map(int, input().split()))
    i = deque(map(str, range(1, n + 1)))
    
    ans = []
    for _ in range(n):
        ans.append(str(i.popleft()))
        
        r = (q[0] > 0) - q.popleft()

        q.rotate(r)
        i.rotate(r)

    return ' '.join(ans)

if __name__ == "__main__":
    print(main())
