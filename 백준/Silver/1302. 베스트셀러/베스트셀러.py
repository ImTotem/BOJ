import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

INF = float('inf')

def main():
    d = defaultdict(int)

    for _ in range(int(input())):
        d[input()] += 1

    return max(sorted(d.items()), key=lambda x:x[1])[0]

if __name__ == "__main__":
    print(main())
