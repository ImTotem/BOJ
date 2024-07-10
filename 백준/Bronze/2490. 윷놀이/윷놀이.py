import sys
input = lambda:sys.stdin.readline().strip()

def main():
    return ["D", "C", "B", "A", "E"][sum(map(int, input().split()))]

for _ in range(3):
    print(main())