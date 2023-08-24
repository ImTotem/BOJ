a = int(input())
b = list(map(int, input().split()))
print(min(a, b[0]//2+b[1]))