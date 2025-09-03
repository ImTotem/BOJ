import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    t = tuple(map(int, input().split()))

    y, m = 0, 0
    for i in t:
        y += i // 30 + 1
        m += i // 60 + 1
    y *= 10
    m *= 15

    ans = []
    if y <= m: ans.append('Y')
    if m <= y: ans.append('M')

    return f"{' '.join(ans)} {min(m, y)}"



if __name__ == "__main__":
    print(main())
