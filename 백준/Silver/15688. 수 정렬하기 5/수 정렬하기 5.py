import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())

    ans = [int(input()) for _ in range(n)]
    ans.sort()

    return '\n'.join(map(str,ans))

print(main())