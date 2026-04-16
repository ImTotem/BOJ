import sys
input = lambda:sys.stdin.readline().strip()

def main():
    ans = []

    for _ in range(int(input())):
        s, t = input().split()
        ans.append(''.join(t[i].upper() for i in range(len(s)) if s[i] in 'xX'))
    
    print(''.join(ans))

main()