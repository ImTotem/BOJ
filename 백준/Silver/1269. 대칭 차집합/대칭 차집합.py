from sys import stdin
input = stdin.readline

nA, nB = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a-b)+len(b-a))