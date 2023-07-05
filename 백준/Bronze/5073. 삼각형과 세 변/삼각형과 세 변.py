import sys
input = lambda:sys.stdin.readline().strip()

while 0 < sum(l:=sorted(map(int, input().split()))):print(["Invalid", ["Equilateral", "Isosceles", "Scalene"][len(set(l))-1]][l[0]+l[1] > l[2]])