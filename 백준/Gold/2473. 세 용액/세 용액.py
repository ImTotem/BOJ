import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    a = sorted(map(int, input().split()))

    ans = [float('inf')]
    for i in range(n-2):
        lo, hi = i+1, n-1
        while lo < hi:
            s = a[i] + a[lo] + a[hi]
            
            if abs(s) < abs(sum(ans)):
                ans = [a[i], a[lo], a[hi]]
            
            if s == 0: return ans

            if 0 < s: hi -= 1
            elif s < 0: lo += 1
    
    return ans

print(*main())