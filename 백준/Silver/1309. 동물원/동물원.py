import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')

def main():
    n = int(input())

    MOD = 9901

    a, b = 1, 1

    for _ in range(n):
        a, b = (a + 2 * b) % MOD, (a + b) % MOD
    
    return a % MOD

if __name__ == "__main__":
    print(main())
