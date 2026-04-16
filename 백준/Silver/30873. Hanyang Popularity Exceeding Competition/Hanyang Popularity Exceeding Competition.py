import sys
input = lambda:sys.stdin.readline().strip()

def main():
    ans = 0

    for _ in range(int(input())):
        p, c = map(int, input().split())
        ans += abs(p-ans) <= c

    print(ans)

main()