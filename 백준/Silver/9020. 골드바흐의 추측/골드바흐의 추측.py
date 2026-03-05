import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict, deque

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    MAX = 10000 + 1
    RSET = lambda a, b, c: set(range(a, b, c))

    prime = {2, 3} | RSET(5, MAX, 6) | RSET(7, MAX, 6)
    for i in range(5, int(MAX ** .5) + 1, 6):
        if i in prime:
            prime -= RSET(i * i, MAX, i * 6) | RSET(i * (i + 2), MAX, i * 6)
        j = i + 2
        if j in prime:
            prime -= RSET(j * j, MAX, j * 6) | RSET(j * (j + 4), MAX, j * 6)

    sp = sorted(prime)

    ans = []
    for _ in range(int(input())):
        n = int(input())
        
        d = INF
        a = [0, 0]
        for i in sp:
            if n - i in prime:
                if n - i == a[0]: break
                if abs(n - i - i) < d:
                    d = abs(n - i - i)
                    a = sorted([i, n - i])
        
        ans.append(' '.join(map(str, a)))

    return '\n'.join(ans)

if __name__ == "__main__":
    print(main())
