from sys import stdin
input = stdin.readline

n = int(input())

length = list(map(int, input().split()))
price = list(map(int, input().split()))[:-1]

_min = min(price)

minPrice = 0
for i in range(n-1):
    if _min == price[i]:
        minPrice+=sum(length[i:])*_min
        break
    else:
        minPrice+=length[i]*price[i]

print(minPrice)