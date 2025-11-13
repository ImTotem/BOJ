import sys
input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left

INF = float('inf')

def main():
    n = int(input())
    a = list(map(int, input().split()))

    dp = []
    
    for i in a:
        if not dp or i > dp[-1]:
            dp.append(i)
        else:
            dp[bisect_left(dp, i)] = i
            
    return len(dp)

if __name__ == "__main__":
    print(main())
