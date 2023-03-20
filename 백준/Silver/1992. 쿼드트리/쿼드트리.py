from sys import stdin
input = stdin.readline

n = int(input())

_vdieo = [list(input())[:-1] for _ in range(n)]

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

def func(video, n):
    if chk(video):return f"{video[0][0]}"

    result = "("
    for i in resize(video, n):
        if chk(i):
            result += i[0][0]
        else:
            result += func(i, n//2)
    
    return result + ")"
            

print(func(_vdieo, n))