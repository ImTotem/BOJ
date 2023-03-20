from sys import stdin
input = stdin.readline

case = 0
while True:
    n0 = int(input())
    if n0:
        case += 1
        n1 = 3*n0
        n2 = n1//2 if n1 % 2 == 1 else (n1+1)//2
        n3 = 3*n2
        n4 = n3//9

        print(f"{case}. {'even' if not n1%2 else 'odd'} {n4}")
    else:
        break