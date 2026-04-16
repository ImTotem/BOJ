import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    T = map(int, input().split())
    t, p  = map(int, input().split())
    print(sum(i//t + (i%t!=0) for i in T))
    print(n // p, n%p)

main()