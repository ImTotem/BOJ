import sys
input = lambda: sys.stdin.readline().strip()

from collections import deque

INF = float('inf')

def main():
    n = int(input())
    q = deque()
    while (p := input()) != '-1':
        if p == '0': q.popleft()
        elif len(q) < n: q.append(p)
    
    if not q: return 'empty'

    return ' '.join(q)

if __name__ == "__main__":
    print(main())
