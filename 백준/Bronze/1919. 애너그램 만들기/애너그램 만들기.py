import sys
input = lambda: sys.stdin.readline().strip()
from collections import Counter

INF = float('inf')

def main():
    a = Counter(input())
    for i in input():
        a[i] -= 1
    
    return sum(map(abs, a.values()))

if __name__ == "__main__":
    print(main())
