import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, l = map(int, input().split())
    
    s = lambda start, length: length * (2 * start + length - 1) // 2

    for i in range(l, 101):
        lo, hi = 0, n + 1

        while lo < hi:
            mid = (lo + hi) // 2
            res = s(mid, i)
            if res < n:
                lo = mid + 1
            elif res == n:
                return ' '.join(str(j) for j in range(mid, mid+i))
            else:
                hi = mid

    return -1
    
if __name__ == "__main__":
    print(main())
