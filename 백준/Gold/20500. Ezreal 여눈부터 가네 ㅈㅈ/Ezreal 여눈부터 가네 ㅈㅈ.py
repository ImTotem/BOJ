import sys
input = lambda:sys.stdin.readline().strip()

MOD = 1000000007

def main():
    n = int(input())

    ans = 0
    for i in range(n-1):
        ans = (ans * 2 + [1, -1][i%2]) % MOD
    
    return ans

print(main())