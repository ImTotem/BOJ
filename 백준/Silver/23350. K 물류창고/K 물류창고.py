import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque
from bisect import bisect_left

INF = float('inf')

def main():
    n, m = map(int, input().split())
    cont = deque(tuple(map(int, input().split())) for _ in range(n))

    order = sorted(map(lambda x:x[0], cont))

    ans = 0

    stack = []
    while cont:
        while cont[0][0] != order[-1]:
            ans += cont[0][1]
            cont.rotate(-1)
        
        p, w = cont.popleft()

        if m != order.pop():
            stack = []
            m = p
        
        idx = bisect_left(stack, w)
        ans += w + 2 * sum(stack[:idx])
        stack.insert(idx, w)

    return ans

if __name__ == "__main__":
    print(main())
