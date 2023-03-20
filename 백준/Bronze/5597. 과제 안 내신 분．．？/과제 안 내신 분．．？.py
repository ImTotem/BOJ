from sys import stdin
input = stdin.readline

print(*sorted(set(range(1, 31, 1)) - set(int(input()) for _ in range(28))), sep="\n")