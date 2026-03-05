import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict, deque

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    n, k = map(int, input().split())
    dq = deque(range(1, n + 1))

    ans = []

    while dq:
        dq.rotate(-k + 1)
        ans.append(str(dq.popleft()))

    return f'<{", ".join(ans)}>'

if __name__ == "__main__":
    print(main())
