import sys
input = lambda:sys.stdin.readline().strip()

def main():
    s = input()
    t = input()

    while s != t and t:
        t = t[:-1] if t[-1] == 'A' else t[::-1][1:]

    return int(s == t)

print(main())