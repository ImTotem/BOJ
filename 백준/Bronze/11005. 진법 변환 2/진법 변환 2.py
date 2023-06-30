import sys
input = lambda:sys.stdin.readline().strip()

n, b = map(int, input().split())
digs = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convert(n, base):
    q, r = divmod(n, base)

    return convert(q, base) + digs[r] if q else digs[r]

print(convert(n, b))