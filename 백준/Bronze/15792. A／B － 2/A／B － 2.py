from decimal import Decimal, getcontext
getcontext().prec = 2000
a, b = map(Decimal, input().split())
print(a/b)