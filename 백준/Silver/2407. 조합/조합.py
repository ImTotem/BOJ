from math import factorial as f
n, m = list(map(int, input().split()))
print(f(n)//(f(n-m)*f(m)))
