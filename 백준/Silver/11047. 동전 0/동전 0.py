import sys

count = 0

n, k = list(map(int, sys.stdin.readline().split()))
li = []
for i in range(n):
    li.insert(0, int(sys.stdin.readline()))

i = 0
while k > 0:
    if li[i] <= k:
        count += k//li[i]
        k-=k//li[i]*li[i]
        if li[i] <= k:
            continue
    i+=1
print(count)