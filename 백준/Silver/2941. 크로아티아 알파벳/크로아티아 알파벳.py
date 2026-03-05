import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict, deque

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    a = input()

    rep = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for r in rep:
        a = a.replace(r, '0')

    return len(a)

if __name__ == "__main__":
    print(main())
