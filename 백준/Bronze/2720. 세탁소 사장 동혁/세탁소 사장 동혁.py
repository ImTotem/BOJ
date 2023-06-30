import sys
input = lambda:sys.stdin.readline().strip()

for _ in range(int(input())):
    c = int(input()) # penny = c
    quarter, c = divmod(c, 25)
    dime, c = divmod(c, 10)
    nickel, c = divmod(c, 5)
    
    print(quarter, dime, nickel, c)