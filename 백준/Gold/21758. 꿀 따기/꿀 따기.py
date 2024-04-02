import sys
input = lambda:sys.stdin.readline().strip()

from itertools import accumulate

def main():
    n = int(input())
    honey = list(map(int, input().split()))

    acc = list(accumulate(honey))
    
    ans = 0
    for i in range(1, n-1):
        ans = max(
            ans,
            2*acc[-1] - honey[0] - honey[i] - acc[i],
            acc[i-1] + acc[-2] - honey[i],
            acc[i] - honey[0] + acc[-2] - acc[i-1]
        )

    return ans

print(main())