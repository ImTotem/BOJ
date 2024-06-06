import sys
input = lambda:sys.stdin.readline().strip()

def main():
    leap = lambda x:(x % 400 == 0) or (x % 4 == 0 and x % 100 != 0)
    ans = 29 + leap(int(input()))
    input()
    
    return ans

print(main())