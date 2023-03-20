from sys import stdin
input = stdin.readline

n = int(input())

li = [0 for _ in range(n+1)]
li[1] = 1

for i in range(2, n+1):
    m = 4
    
    j = 1
    while j**2 <= i:
        m = min(m, li[i-j**2])
        j += 1
    li[i] = m+1

print(li[n])