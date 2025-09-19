import sys
input = lambda: sys.stdin.readline().strip()
from bisect import bisect_left

INF = float('inf')

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [a[0]]
    for i in range(1, n):
        if dp[-1] < a[i]:
            dp.append(a[i])
        else:
            dp[bisect_left(dp, a[i])] = a[i]
    
    return len(dp)

if __name__ == "__main__":
    print(main())
