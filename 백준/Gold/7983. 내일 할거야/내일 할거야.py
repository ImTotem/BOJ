import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    a = [tuple(map(int, input().split())) for _ in range(n)]
    a.sort(key=lambda x:(-x[1],-x[0]))

    ans = a[0][1]

    for d, t in a:
        ans = min(ans, t)-d

    print(ans)

main()
