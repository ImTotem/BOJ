import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    m, n = map(int, input().split())
    ll = list(map(int, input().split()))
    
    lo, hi = 1, max(ll)
    while lo <= hi:
        mid = (lo + hi) // 2

        l = sum(i // mid for i in ll)
        
        if l < m:
            hi = mid - 1
        else:
            lo = mid + 1
        
    return hi
    
if __name__ == "__main__":
    print(main())
