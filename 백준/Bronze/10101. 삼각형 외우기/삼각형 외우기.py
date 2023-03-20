a=[int(input())for _ in range(3)]
print("Error"if sum(a)!=180 else"Equilateral"if len(set(a))==1 else"Isosceles"if len(set(a))==2 else"Scalene")