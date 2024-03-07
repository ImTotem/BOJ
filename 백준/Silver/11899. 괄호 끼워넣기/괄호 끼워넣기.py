import sys
input = lambda:sys.stdin.readline().strip()

def main():
    s = input()
    while '()' in s:
        s = s.replace('()', '')
    
    print(len(s))

main()