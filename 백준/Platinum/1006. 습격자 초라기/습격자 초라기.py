import sys
input = lambda:sys.stdin.readline().strip()

def main():
    for _ in range(int(input())):
        n, w = map(int, input().split())
        s = [list(map(int, input().split())) for _ in range(2)]

        if n == 1:
            print(1 + (w < sum(sum(s, []))))
            continue
        
        ans = float('inf')
        for f in [2, 2], [1, 2], [2, 1], [1, 1]:
            flag = False
            for i in range(2):
                if f[i] == 1 and w < sum(s[i][::n-1]): flag = True
            if flag: continue
            
            dp = [[0] * 3 for _ in range(n)]
            dp[0] = [1, 1, 2 - ((S:=sum(f)) == 4 and s[0][0] + s[1][0] <= w)]
            dp[1] = [
                a:=3 - (f[0] == 2 and sum(s[0][:2]) <= w),
                b:=3 - (f[1] == 2 and sum(s[1][:2]) <= w),
                min(3 + (w < s[0][1] + s[1][1]), min(a,b)+1)
            ]

            for i in range(1 + (S != 4), n):
                dp[i] = [
                    c:=min(dp[i-1][2], dp[i-1][1] + (a:=w < sum(s[0][i-1:i+1]))) + 1,
                    d:=min(dp[i-1][2], dp[i-1][0] + (b:=w < sum(s[1][i-1:i+1]))) + 1,
                    min(dp[i-1][2] + 1 + (w < s[0][i] + s[1][i]), min(c,d)+1, dp[i-2][2]+2+a+b)
                ]

            if S == 4: ans = min(ans, dp[-1][2])
            elif S == 2: ans = min(ans, dp[-2][2])
            else: ans = min(ans, dp[-1][f[0] == 1])
            
        print(ans)
main()