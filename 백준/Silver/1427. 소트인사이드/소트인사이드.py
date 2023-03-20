from sys import stdin
input = stdin.readline

print(int(''.join(i for i in sorted(list(input().replace("\n", "")), reverse=True))))