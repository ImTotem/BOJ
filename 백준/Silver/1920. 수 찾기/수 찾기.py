from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))

m = int(input())
for i in list(map(int, input().split())):
    print(1 if i in a else 0)