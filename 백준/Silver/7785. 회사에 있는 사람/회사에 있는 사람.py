from sys import stdin
input = stdin.readline

n = int(input().rstrip())
dic = dict()
for i in range(n):
	a = input().split()
	if a[1] == "enter":
		dic[a[0]] = True
	else:
		del dic[a[0]]

print("\n".join(sorted(dic.keys(), reverse=True)))