import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())

    a, b = [[], [1]] 

    for i in range(2, n+1):
        a, b = b, [i-1, *a[::-1], i]
    
    return b
    
print(*main())