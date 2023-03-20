s=0
for i in range(5):
    a = int(input())
    if a < 40: s += 40
    else: s+=a

print(s//5)