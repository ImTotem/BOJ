import sys
input = lambda:sys.stdin.readline().strip()

from bisect import bisect_left

def main():
    n = int(input())
    node = [tuple(map(int, input().split())) for _ in range(n)]
    node.sort(key=lambda x:x[0])

    dp = [node[0][1]]

    for i in range(n):
        if dp[-1] < node[i][1]: dp.append(node[i][1])
        else: dp[bisect_left(dp, node[i][1])] = node[i][1]
    
    print(n-len(dp))

main()