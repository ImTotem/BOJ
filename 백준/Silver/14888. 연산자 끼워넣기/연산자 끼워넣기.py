from itertools import permutations as perm
from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
o = list(map(int, input().split()))
oper = ["+-*/"[i] for i in range(4) for _ in range(o[i])]

oper = list(set(perm(oper, n-1)))

def calc(f:list):
    length = len(f)
    c = f[0][0]
    op = ''

    for i in range(1, length):
        op = f[i-1][1]
        temp = f[i][0] if i < length - 1 else f[i]

        if op == "/":
            if c < 0 and temp > 0:
                c = -(-c // temp)
            else:
                c //= temp
        else:
            c = eval(f"{c}{op}{temp}")



    return c

answer = [calc(list(zip(a, opers))+[a[-1]]) for opers in oper]

print(max(answer))
print(min(answer))