import sys
input = lambda:sys.stdin.readline().strip()
from re import sub
def main():
    input()
    a = input().split()
    m = len(max(a, key=len))
    a.sort(key=lambda x:x*m)

    print(int(''.join(a[::-1])))

main()