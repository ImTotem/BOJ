import sys
input = lambda: sys.stdin.readline().strip()

def main():
    k, n = map(int, input().split())
    lans = [int(input()) for _ in range(k)]

    lo, hi = 1, max(lans)
    while lo <= hi:
        mid = (lo + hi) // 2

        amount = sum(lan // mid for lan in lans)

        if amount < n:
            hi = mid - 1
        else:
            lo = mid + 1
    
    return hi
    
if __name__ == "__main__":
    print(main())
