import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    x, y = map(int, input().split())

    if x == y: return -1

    f = lambda a: int((y + a) * 100 / (x + a))
    
    c = f(0)

    lo, hi = 0, 1000000001
    ans = hi
    while lo <= hi:
        mid = (lo + hi) // 2

        if f(mid) > c:
            ans = min(ans, mid)
            hi = mid - 1
        else:
            lo = mid + 1
        
    return ans if f(ans) != c else -1

if __name__ == "__main__":
    print(main())
