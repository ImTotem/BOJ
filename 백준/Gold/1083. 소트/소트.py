import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = int(input())

    target = sorted(a)

    ans = []

    r = n - 1
    while s and r != 0:
        idx = a.index(target[r])
        
        if idx > s:
            r -= 1
        else:
            ans.append(str(a.pop(idx)))
            target.pop(r)
            s -= idx
            n -= 1
            r = len(target) - 1
    
    ans += map(str, a)

    return ' '.join(ans)


if __name__ == "__main__":
    print(main())
