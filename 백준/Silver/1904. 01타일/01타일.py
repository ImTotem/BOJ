import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')

def main():
    n = int(input())
    MOD = 15746
    if n <= 2: return n

    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, (a + b) % MOD
    
    return b % MOD

if __name__ == "__main__":
    print(main())
