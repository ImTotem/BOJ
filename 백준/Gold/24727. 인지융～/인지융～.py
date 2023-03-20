from sys import stdin
input = stdin.readline

n = int(input())
c, e = map(int, input().split())

if n*n - (c+e) < n:
    print(-1)
else:
    print(1)
    l = ('1'*c)+('0'*n)+('2'*e)+('0'*(n*n-c-e-n))

    for i in range(n):
        print(l[i*n:i*n+n])