import sys
input = lambda:sys.stdin.readline().strip()

def main():
    print(*min([tuple(map(int, input().split())) for _ in range(int(input()))], key=lambda x:x[1]))
main()