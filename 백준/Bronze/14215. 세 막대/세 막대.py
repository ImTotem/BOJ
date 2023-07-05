import sys
input = lambda:sys.stdin.readline().strip()

l = sorted(map(int, input().split()))
print(min(sum(l), 2*sum(l[:2])-1))