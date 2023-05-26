import sys
input = lambda: sys.stdin.readline().strip()

print(str(bin(int(input(), 8))).replace("0b",""))