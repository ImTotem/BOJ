a = 0
b = 0

for i in range(9):
    c = int(input())
    if c > a:
        a = c
        b = i+1
print(a)
print(b)