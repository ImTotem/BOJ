import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    ps = [tuple(map(int, input().split())) for _ in range(n)]
    ps.sort()

    d = lambda a, b: (a - b) ** 2
    dist = lambda p, q: d(p[0], q[0]) + d(p[1], q[1])
    
    def dq(lo, hi):
        if lo == hi: return INF
        if hi - lo == 1: return dist(ps[lo], ps[hi])

        mid = (lo + hi) // 2
        ans = min(dq(lo, mid), dq(mid + 1, hi))
        
        cand = [ps[i] for i in range(lo, hi + 1) if d(ps[i][0], ps[mid][0]) < ans]
        cand.sort(key=lambda x:x[1])

        for i in range(len(cand) - 1):
            for j in range(i + 1, len(cand)):
                if d(cand[i][1], cand[j][1]) < ans:
                    ans = min(ans, dist(cand[i], cand[j]))
                else:
                    break

        return ans

    return dq(0, n - 1)


if __name__ == "__main__":
    print(main())
