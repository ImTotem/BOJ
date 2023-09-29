import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())
    print(["Can win", "Can't win"][n % (m+1) == 1])

main()