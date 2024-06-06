import sys
input = lambda:sys.stdin.readline().strip()

def main():
    k = int(input())
    a, b, c, d = map(int, input().split())

    return [("No",), ("Yes", (x:=a * k + b))][x == c * k + d]

print(*main())