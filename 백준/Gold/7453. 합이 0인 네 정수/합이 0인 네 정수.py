import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    arr = tuple(map(sorted, zip(*arr)))

    ab = sorted(a+b for a in arr[0] for b in arr[1])
    cd = sorted(c+d for c in arr[2] for d in arr[3])
    
    ans = 0

    l, r = 0, len(cd) - 1
    
    while l < len(ab) and 0 <= r:
        if (s := ab[l] + cd[r]) == 0:
            nl, nr = l+1, r-1
            while nl < len(ab) and ab[l] == ab[nl]:
                nl += 1
            while 0 <= nr and cd[r] == cd[nr]:
                nr -= 1
            ans += (nl-l) * (r-nr)
            l, r = nl, nr
        elif s < 0:
            l += 1
        else:
            r -= 1

    return ans

print(main())