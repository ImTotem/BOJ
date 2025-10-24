import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

INF = float('inf')

def main():
    n = int(input())
    a = list(map(int, input().split()))

    dq = deque()
    for i in range(n - 1, -1, -1):
        if a[i] == 1: dq.appendleft(n - i)
        elif a[i] == 2: dq.insert(1, n - i)
        else: dq.append(n - i)
    
    return ' '.join(map(str, dq))

if __name__ == "__main__":
    print(main())
