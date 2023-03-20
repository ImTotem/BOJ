n = int(input())

f = [0, 1, 1]
for i in range(n-2):
    f.append(f[-1] + f[-2])
print(f[n])