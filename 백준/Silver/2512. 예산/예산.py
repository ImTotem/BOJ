import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    budgets = list(map(int, input().split()))
    m = int(input())

    budgets.sort()

    ans = -INF
    summ = 0
    for i in range(n):
        ans = max(ans, (m - summ) // (n - i))
        summ += budgets[i]

    return min(ans, budgets[-1])
    
if __name__ == "__main__":
    print(main())
