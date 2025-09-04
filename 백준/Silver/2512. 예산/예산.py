import sys
input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    budgets = list(map(int, input().split()))
    m = int(input())

    lo, hi = 1, max(budgets)
    while lo <= hi:
        mid = (lo + hi) // 2

        budget = sum(min(i, mid) for i in budgets)

        if budget > m:
            hi = mid - 1
        else:
            lo = mid + 1
    
    return hi
    
if __name__ == "__main__":
    print(main())
