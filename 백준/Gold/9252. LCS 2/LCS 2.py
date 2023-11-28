import sys
input = lambda:sys.stdin.readline().strip()

def main():
    s1, s2 = input(), input()
    x, y = len(s1), len(s2)
    dp = [[''] * (x+1) for _ in range(y+1)]

    for i in range(1, y+1):
        for j in range(1, x+1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], key=len)
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1] + s1[j-1]
    
    print(len(dp[y][x]), dp[y][x], sep="\n")

main()