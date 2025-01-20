import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    a = list(map(int, input().split()))

    def can_heat_all(t):
        lo, hi = 0, n - 1
        
        for i in range(n):
            d = t // a[i]
            
            new_lo = max(0, i - d)
            new_hi = min(n-1, i + d)
            
            lo = max(lo, new_lo)
            hi = min(hi, new_hi)
            
            if lo > hi:
                return False
        
        return True

    
    lo, hi = 0, max(a) * (n - 1)
    ans = hi
    while lo <= hi:
        mid = (lo + hi) // 2

        if can_heat_all(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    
    return ans

if __name__ == "__main__":
    print(main())
