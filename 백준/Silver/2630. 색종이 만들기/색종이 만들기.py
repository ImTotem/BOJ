from sys import stdin
input = stdin.readline

n = int(input())

_paper = [input().split() for _ in range(n)]

def chk(p):
    flag = '0' if int(p[0][0]) else '1'
    for i in p:
        if flag in i:
            return False
    return True

def resize(p, n):
    size = n//2
    slices = []
    
    first = slice(0, size)
    second = slice(size, size*2)

    for i in [p[first], p[second]]:
        a, b = [j[first] for j in i], [j[second] for j in i]
        slices.append(a)
        slices.append(b)
    
    return slices

def func(paper, n):
    white, blue = 0, 0
    for i in resize(paper, n):
        if chk(i):
            if int(i[0][0]):
                blue += 1
            else:
                white += 1
        else:
            w,b = func(i, n//2)
            white+=w
            blue+=b
    
    return (white, blue)
            

if chk(_paper):
    if int(_paper[0][0]):
        print(0),print(1)
    else:
        print(1),print(0)
else:
    white, blue = func(_paper, n)
    print(white)
    print(blue)