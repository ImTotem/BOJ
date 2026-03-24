import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
from itertools import permutations as perm
from heapq import heappop, heappush

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    h, w = map(int, input().split())

    ans = [[] for _ in range(h)]

    for y in range(h):
        c = input()
        
        idx = -1
        for x in range(w):
            if c[x] == 'c':
                idx = x
            
            if idx == -1:
                ans[y].append('-1')
            else:
                ans[y].append(str(x - idx))
    
    return '\n'.join(' '.join(i) for i in ans)


if __name__ == "__main__":
    print(main())
