import sys
input = lambda:sys.stdin.readline().strip()


w, h = map(int, input().split())
print(f"{w*h/2:.1f}")
