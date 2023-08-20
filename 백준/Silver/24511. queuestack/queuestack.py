import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())

a = list(map(int, input().split()))
questack = list(map(int, input().split()))

m = int(input())
c = list(map(int, input().split()))

que = [questack[i] for i in range(n) if a[i] == 0][::-1] + c
print(*que[:m])