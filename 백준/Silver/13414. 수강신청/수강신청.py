import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

INF = float('inf')

def main():
    k, l = map(int, input().split())

    s = defaultdict(int)
    for i in range(l):
        sid = input()
        s[sid] = i
        
    return '\n'.join(
        map(
            lambda x: x[0],
            sorted(s.items(), key=lambda x: x[1])[:k]
        )
    )

if __name__ == "__main__":
    print(main())
