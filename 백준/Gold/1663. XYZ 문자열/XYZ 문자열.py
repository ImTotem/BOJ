import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    prob = int(input())
    n = int(input())
    k = None
    if prob == 2:
        k = int(input())
    elif prob == 3:
        k = input()
    
    N = 100

    # S(n) = S(n - 3) + S(n - 2)
    dp = [0] * (N + 1)
    dp[1] = 1
    
    x, y, z = 1, 0, 0
    for i in range(2, n + 1):
        x, y, z = z, x, y + x
        dp[i] = x + y + z
    
    if prob == 1:
        return dp[n]
    elif prob == 3:
        return (x, y, z)['XYZ'.index(k)]
    
    # prob == 2
    while n > 3:
        left = dp[n - 3]

        if left < k:
            n -= 2
            k -= left
        else:
            n -= 3
    
    if n == 1: return 'X'
    if n == 2: return 'YZ'[k - 1]
    return 'ZX'[k - 1] # n == 3


if __name__ == "__main__":
    print(main())
