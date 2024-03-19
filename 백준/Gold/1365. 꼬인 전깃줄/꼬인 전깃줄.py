import sys
input = lambda:sys.stdin.readline().strip()

from bisect import bisect_left

def main():
    n = int(input())
    a = tuple(map(int, input().split()))

    dp = [a[0]]

    for i in range(n):
        if dp[-1] < a[i]: dp.append(a[i])
        else: dp[bisect_left(dp, a[i])] = a[i]
    
    print(n-len(dp))

main()