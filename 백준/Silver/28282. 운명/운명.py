import sys
input = lambda:sys.stdin.readline().strip()

x, k = map(int, input().split())
a = list(map(int, input().split()))

left, right = a[:x], a[x:]
left.sort(); right.sort()

left_k = [0] * (k+1)
right_k = [0] * (k+1)

for i in range(x):
    left_k[left[i]] += 1
    right_k[right[i]] += 1

ans = x**2
for i in set(left):
    ans -= left_k[i] * right_k[i]

print(ans)