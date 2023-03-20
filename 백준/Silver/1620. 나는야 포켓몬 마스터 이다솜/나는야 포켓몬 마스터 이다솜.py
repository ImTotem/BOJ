from sys import stdin
input = stdin.readline

n, m = list(map(int, input().split()))

li = []
li2 = {}
for i in range(n):
	a = input().rstrip()
	li.append(a)
	li2[a] = i+1

for i in range(m):
	a = input().rstrip()
	if a.isdigit():
		print(li[int(a)-1])
	else:
		print(li2[a])