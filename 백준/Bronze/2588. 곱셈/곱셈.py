a = int(input())
b = input()
li = []
for i in b:
    li.append(a * int(i))
li.reverse()
for i in li:
    print(i)
print(a*int(b))