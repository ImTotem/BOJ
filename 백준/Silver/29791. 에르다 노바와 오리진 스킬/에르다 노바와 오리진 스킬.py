import sys
input = lambda:sys.stdin.readline().strip()

n, m = map(int, input().split())

a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))

cnt1 = 1
cnt2 = 1

atk1, atk2 = a[0], b[0]
for i in range(1, n):
    if 100 <= a[i] - atk1:
        cnt1 += 1
        atk1 = a[i]

for i in range(1, m):
    if 360 <= b[i] - atk2:
        cnt2 += 1
        atk2 = b[i]

print(cnt1, cnt2)
