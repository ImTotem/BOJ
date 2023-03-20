n = int(input())

a = n*2-1

for i in range(n):
    print(' '*i +'*'*(a-(i*2)))

for i in range(n-2, -1, -1):
    print(' '*i + '*'*(a-(i*2)))
