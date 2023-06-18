import sys

input = lambda: sys.stdin.readline().strip()

round_ = lambda n: int(n)+[0, 1][0.5 <= n-int(n)]

n = int(input())
opinion = sorted(int(input()) for _ in range(n))
cut = round_(n*0.15)

print(round_(sum(opinion[i] for i in range(cut, n-cut)) / (n-cut*2)) if (n-cut*2) != 0 else 0)