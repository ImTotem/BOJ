from sys import stdin
input = stdin.readline

s = input()[:-1]
length = len(s)

print(len(set(s[j:j+i+1] for i in range(length) for j in range(length-i))))