from sys import stdin
input = stdin.readline

n = int(input())

answer = 0
for i in range(1, n+1):
  ans = i+sum(list(map(int, list(str(i)))))

  if ans == n:
    answer = i
    break
  
print(answer)