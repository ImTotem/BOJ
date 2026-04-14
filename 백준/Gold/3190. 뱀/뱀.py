import sys
input = lambda: sys.stdin.readline().rstrip()
from  collections import deque

INF = float('inf')
D = [-1, 0, 1, 0, -1, -1, 1, 1, -1] # 4: 상하좌우, 8: 대각선포함

def main():
    n = int(input())
    k = int(input())
    apples = set(tuple(map(int, input().split())) for _ in range(k))
    l = int(input())
    a = deque([input().split() for _ in range(l)])

    ans = 0
    
    x, y = 0, 0
    dx, dy = 1, 0
    q = deque([(0, 0)])
    while 0 <= x < n and 0 <= y < n:
        ans += 1
        
        # 시뮬
        x, y = x + dx, y + dy
        if not (0 <= x < n and 0 <= y < n):
            break

        if (x, y) in q:
            break

        q.append((x, y))
        if (y+1, x+1) in apples:
            apples.discard((y+1, x+1))
        else:
            q.popleft()
        
        # 방향 전환
        if a and int(a[0][0]) == ans:
            rot = a.popleft()[1]
            dx, dy = (dy, -dx) if rot == 'L' else (-dy, dx)
    
    return ans


if __name__ == "__main__":
    print(main())
