n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
last = []
for i in a:
    if i < x:
        last.append(i)
print(' '.join(str(i) for i in last))
