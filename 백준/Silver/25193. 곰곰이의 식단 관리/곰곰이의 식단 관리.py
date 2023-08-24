from math import ceil
n = int(input())
a = input().count('C')
print(ceil(a/(n-a+1)))