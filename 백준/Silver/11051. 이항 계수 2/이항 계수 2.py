from math import factorial as f

n, k = list(map(int, input().split()))
print(f(n)//(f(k)*f(n-k))%10007)
