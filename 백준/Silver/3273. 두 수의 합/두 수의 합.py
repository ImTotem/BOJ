import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())

    a.sort()
    ans = 0

    l, r = 0, n-1
    while True:
        while l < r and a[l] + a[r] > x:
            r -= 1
        
        if l == r: break

        ans += a[l] + a[r] == x
        l += 1
        
    return ans

if __name__ == "__main__":
    print(main())
