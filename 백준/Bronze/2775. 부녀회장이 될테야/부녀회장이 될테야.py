from sys import stdin
input = stdin.readline

li = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]

for i in range(1, 15):
	li.append([])
	for j in range(1, 15):
		li[i].append(sum(li[i-1][:j]))

T = int(input())
for _ in range(T):
	k = int(input())
	n = int(input())

	print(li[k][n-1])