import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque
from bisect import bisect_left

INF = float('inf')

def main():
    n, m = map(int, input().split())
    cont = deque(tuple(map(int, input().split())) for _ in range(n))
    # (우선순위 p, 무게 w)

    order = sorted(map(lambda x:x[0], cont))

    ans = 0

    stack = []
    while cont:
        while cont[0][0] != order[-1]:
            ans += cont[0][1]
            cont.rotate(-1)
        
        p, w = cont.popleft()
        order.pop()

        if stack and stack[-1][0] != p:
            stack = []
        
        idx = bisect_left(stack, w, key=lambda x:x[1])
        ans += w + 2 * sum(map(lambda x:x[1], stack[:idx]))
        stack.insert(idx, (p, w))

    return ans

if __name__ == "__main__":
    print(main())
