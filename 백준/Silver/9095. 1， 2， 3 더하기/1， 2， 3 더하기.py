import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')

def main():
    n = int(input())
    dp = [0, 1, 2, 4]
    
    for _ in range(4, n + 1):
        dp.append(dp[-1] + dp[-2] + dp[-3])
    
    return dp[n]

if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
