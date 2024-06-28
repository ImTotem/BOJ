import sys
input = lambda:sys.stdin.readline().strip()
MIN = -1000000001

def main():
    n = int(input())
    pos = sorted(tuple(map(int, input().split())) for _ in range(n))

    ans = 0
    start, end = MIN, MIN

    for x, y in pos:
        if end < x:
            ans += end - start
            start = x
        if end < y: end = y
    
    return ans + end - start

print(main())