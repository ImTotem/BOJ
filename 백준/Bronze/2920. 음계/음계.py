from sys import stdin
input = stdin.readline

a = list(map(int, input().split()))
b = list(range(1, 9))
print([["mixed", "descending"][a[::-1] == b], "ascending"][a == b])