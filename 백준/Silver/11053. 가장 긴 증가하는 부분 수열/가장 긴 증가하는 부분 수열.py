from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))

lis = [a[0]]
right = 1

def search(right, target):
    left = 0
    while left < right:
        mid = ( left + right ) // 2

        if lis[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return right

for i in range(1, n):
    if lis[-1] < a[i]:
        lis.append(a[i])
        right += 1
    else:
        idx = search(right, a[i])
        lis[idx] = a[i]

print(right)