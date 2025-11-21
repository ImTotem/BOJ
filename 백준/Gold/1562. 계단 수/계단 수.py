import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')

def main():
    n = int(input())
    
    MOD = 1_000_000_000
    
    dp = [[[0] * 4 for _ in range(10)] for _ in range(n)]

    mask = lambda x: {0: 1, 9: 2}.get(x, 0)

    def f(idx, num, bit):
        if dp[idx][num][bit]: return dp[idx][num][bit]
        if idx == n - 1: return bit == 3
        
        if 0 < num:
            dp[idx][num][bit] += f(idx+1, num-1, bit|mask(num-1))
            dp[idx][num][bit] %= MOD

        if num < 9:
            dp[idx][num][bit] += f(idx+1, num+1, bit|mask(num+1))
            dp[idx][num][bit] %= MOD
        
        return dp[idx][num][bit]
    
    ans = 0
    for i in range(1, 10):
        ans = (ans + f(0, i, mask(i))) % MOD
    
    return ans % MOD

if __name__ == "__main__":
    print(main())
