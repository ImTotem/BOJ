import math

d, h, w = map(int, input().split())

a=d/(h**2+w**2)**(1/2)
print(math.floor(h*a), math.floor(w*a))