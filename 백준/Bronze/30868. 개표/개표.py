import sys
input = lambda:sys.stdin.readline().strip()

def main():
    for _ in range(int(input())):
        n = int(input())
        print(*["+"*4] * (n // 5), '|'*(n%5))

main()