from sys import stdin
input = stdin.readline

input()
print(sum((ord(s)-96)*31**i for i, s in enumerate(input().strip())) % 1234567891)