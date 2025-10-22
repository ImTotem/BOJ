import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

INF = float('inf')

def main():
    n, m = map(int, input().split())
    cont = deque(tuple(map(int, input().split())) for _ in range(n))
    # (우선순위 p, 무게 w)

    order = sorted(map(lambda x:x[0], cont))

    ans = 0

    space = []
    stack = []
    while cont:
        while cont[0][0] != order[-1]:
            ans += cont[0][1]
            cont.rotate(-1)
        
        p, w = cont.popleft()
        order.pop()

        if stack and stack[-1][0] != p:
            stack = []
        
        while stack and stack[-1][1] < w:
            ans += stack[-1][1]
            space.append(stack.pop())

        stack.append((p, w))
        ans += w

        while space:
            ans += space[-1][1]
            stack.append(space.pop())

    return ans

if __name__ == "__main__":
    print(main())
