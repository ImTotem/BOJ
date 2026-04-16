import sys
input = lambda:sys.stdin.readline().strip()
from math import ceil

def main():
    n = int(input())
    s = list(map(int, input().split()))
    
    for _ in range(int(input())):
        a, b = map(int, input().split())

        if a == 1:
            for i in range(b-1, n, b):
                s[i] = not s[i]
        else:
            b -= 1
            s[b] = not s[b]
            for i in range(1, min(b+1, n-b)):
                if s[b-i] == s[b+i]:
                    s[b-i] = not s[b-i]
                    s[b+i] = not s[b+i]
                else: break
    
    s = list(map(int, s))
    for i in range(ceil(n/20)):
        print(*s[20*i:20*(i+1)])

main()