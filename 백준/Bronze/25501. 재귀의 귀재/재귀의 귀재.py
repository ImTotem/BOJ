import sys
input = lambda:sys.stdin.readline().strip()

def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

for _ in range(int(input())):
    cnt = 0
    print(recursion(s:=input(), 0, len(s)-1), cnt)