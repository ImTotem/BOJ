import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n, f = input(), int(input())

    ans = "00"

    pre = n[:-2]
    for i in range(100):
        suf = str(i).zfill(2)
        if int(pre + suf) % f == 0:
            ans = suf
            break

    return ans

print(main())