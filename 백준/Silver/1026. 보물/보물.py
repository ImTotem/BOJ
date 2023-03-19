from sys import stdin
input = stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

print(sum(map(lambda x:x[0]*x[1], zip(a,b))))