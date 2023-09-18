import sys
input = lambda:sys.stdin.readline().strip()

n, m = map(int, input().split())

li = list(map(int, input().split()))
li.sort()

def search(a):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if li[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    
    if n == end: end -= 1
    elif -1 == end: end += 1
    if -1 == start: start += 1
    elif n == start: start -= 1

    return end, start

P = 0

for _ in range(m):
    a, w = map(int, input().split())
    
    left, right = search(a)

    l, r = abs(li[left] - a) * w, abs(li[right] - a) * w

    P = max(P, min(l, r))

print(P)
