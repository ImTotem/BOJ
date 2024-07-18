import sys
input = lambda:sys.stdin.readline().strip()

def main():
    an, bn = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    return sorted(a - b)

ans = main()
print(len(ans))
if ans:
    print(*ans)