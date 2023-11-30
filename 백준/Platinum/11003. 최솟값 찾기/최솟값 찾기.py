import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

def main():
    _, l = map(int, input().split())
    a = list(map(int, input().split()))

    ans = []
    dq = deque()

    for i, v in enumerate(a):
        while dq and v < dq[-1][1]: dq.pop()
        dq.append((i, v))
        while dq[0][0] <= i - l: dq.popleft()
        ans.append(dq[0][1])
    
    print(*ans)

main()