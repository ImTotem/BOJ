import sys
input = lambda:sys.stdin.readline().strip()

def main():
    gaji = [input().split() for _ in range(10)]

    for i in range(10):
        if len(set(gaji[i])) == 1: return 1
        if len(set(gaji[j][i] for j in range(10))) == 1: return 1

    return 0

print(main())