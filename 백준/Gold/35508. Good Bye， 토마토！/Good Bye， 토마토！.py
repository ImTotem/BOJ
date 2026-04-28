import sys
input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left

INF = float('inf')
D = [-1, 0, 1, 0, -1, -1, 1, 1, -1]

def main():
    n, d = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(n)]
    li.sort(key=lambda x:x[0])

    m1, m2, midx = [0] * n, [0] * n, [-1] * n

    x, y, z = -1, -1, -1
    for i in range(n):
        a = li[i][1]
        if a > x:
            x, y, z = a, x, i
        elif a > y:
            x, y, z = x, a, z
        
        m1[i], m2[i], midx[i] = x, y, z

    ans = 0
    r = n - 1

    for j in range(n):
        t, a, b = li[j]
        
        if t <= d and a + b > ans:
            ans = a + b
        
        while r >= 0 and li[r][0] > d - t: r -= 1

        if r < 0: continue

        best = m1[r] if midx[r] != j else m2[r]
        
        if best != -1 and best + b > ans:
            ans = best + b

    return ans


if __name__ == "__main__":
    print(main())
