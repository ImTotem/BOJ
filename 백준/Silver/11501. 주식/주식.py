import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')

def main():
    n = int(input())
    stocks = list(map(int, input().split()))

    ans = 0

    maxi = 0
    for i in range(n-1, -1, -1):
        if stocks[i] < maxi:
            ans += maxi - stocks[i]
        maxi = max(maxi, stocks[i])
    
    return ans

if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
