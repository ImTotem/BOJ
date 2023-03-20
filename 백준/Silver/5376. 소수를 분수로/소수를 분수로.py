from math import gcd
import sys

input = lambda: sys.stdin.readline().strip()

def frac(a, b):
    g = gcd(a, b)
    return f"{a//g}/{b//g}"

for _ in range(int(input())):
    demical = input()

    if '(' not in demical:
        print(frac(int(demical[2:]), int('1'+'0'*(len(demical) - 2))))
    else:
        a, b = demical.split('(')
        a = a[2:]
        b = b[:-1]

        c = int(a+b) - int(a if a != '' else '0')
        d = int('9'*len(b) + '0'*len(a))

        print(frac(c, d))