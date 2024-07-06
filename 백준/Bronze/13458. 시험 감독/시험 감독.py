import sys
input = lambda:sys.stdin.readline().strip()

from math import ceil

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b, c = map(int, input().split())

    return sum(
        1 + ceil(max(0, i-b) / c)
        for i in a
    )
 
print(main())