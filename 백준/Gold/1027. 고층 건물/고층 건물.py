import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = [0] * n

    def f(l, r):
        l, r = sorted([l, r])
        y = lambda x: (a[r] - a[l]) / (r - l) * (x - l) + a[l]

        for i in range(l + 1, r):
            if y(i) <= a[i]:
                return False
        
        return True
    
    for i in range(n):
        for j in range(n):
            if j == i: continue
            ans[i] += f(i, j)

    return max(ans)
    
if __name__ == "__main__":
    print(main())
