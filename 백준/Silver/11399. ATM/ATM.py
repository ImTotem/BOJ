n = int(input())
li = list(map(int, input().split()))
li.sort(reverse = True)
a = 0
b = 0
for i in range(n):
    a+=li.pop()
    b+=a
print(b)