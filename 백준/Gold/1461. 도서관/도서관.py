import sys
input = lambda: sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    
    a, b = [], []
    la = 0
    for i in p:
        la = max(la, abs(i))
        if i > 0: a.append(i)
        else: b.append(abs(i))

    a.sort(reverse=True)
    b.sort(reverse=True)

    ans = 0
    for x in a, b:
        for i in range(0, len(x), m):
            ans += x[i] << 1

    return ans - la


if __name__ == "__main__":
    print(main())