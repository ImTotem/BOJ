import sys
input = lambda:sys.stdin.readline().strip()

MOD = 1000000007

def power(a, b):
    return (a if b == 1 else (a * power(a, b-1) if b % 2 else (p:=power(a, b//2)) * p)) % MOD

def main():
    m = int(input())

    ans = 0
    for _ in range(m):
        n, s = map(int, input().split())
        ans += s * power(n, MOD-2) % MOD
    
    print(ans % MOD)

main()