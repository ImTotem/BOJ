import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    a = list(map(int, input().split())) + [0, 0]
    
    ans = 0
    for i in range(n):
        if a[i+1] > a[i+2]:
            m = min(a[i], a[i+1]-a[i+2])
            a[i] -= m; a[i+1] -= m
            ans += m * 5
        for k in range(3, 0, -1):
            m = min(a[i:i+k])
            for j in range(k):a[i+j]-=m
            ans += m * [3,5,7][k-1]

    print(ans)
main()
