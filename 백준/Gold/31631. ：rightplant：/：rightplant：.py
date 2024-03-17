import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

def main():
    n = int(input())

    dp = [[], [1]]

    for i in range(2, n+1):
        dp.append([i-1] + dp[i-2][::-1] + [i])
    
    return dp[n]
    
print(*main())