import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n, _, _ = map(int, input().split())
    x1 = sorted(map(int, input().split()))
    x2 = sorted(map(int, input().split()))
    
    n -= (t:=n%2)
    ans = x1.pop() if t else 0

    for _ in range(0, n, 2):
        ans += max(
            (c1 := x1[-2] + x1[-1] if 1 < len(x1) else 0),
            (c2 := x2[-1] if x2 else 0)
        )

        if c2 < c1: x1.pop(); x1.pop()
        else: x2.pop()
    
    print(ans)

main()