import sys
input = lambda:sys.stdin.readline().strip()

from bisect import bisect_left as search

def main():
    n = int(input())
    a = [tuple(map(int, input().split())) for _ in range(n)]
    a.sort()

    dp, idx = [], []

    for i in a:
        cur = search(dp, i[1], key=lambda x:x[1])
        if len(dp) <= cur:
            dp.append(i)
        else:
            dp[cur] = i
        idx.append(cur)
        
    res = []
    m = max(idx)
    for i in range(len(idx)-1, -1, -1):
        if idx[i] == m:
            res.append(a[i][0])
            m-=1
    
    ans = sorted(set(map(lambda x:x[0], a)) - set(res))

    return str(len(ans)) + '\n' + '\n'.join(map(str, ans))

if __name__ == "__main__": 
    print(main())
