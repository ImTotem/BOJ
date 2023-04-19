import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
budget = list(map(int, input().split()))
budget.sort()
m = int(input())

answer = float('-inf')

sum_budget = 0
for i in range(n):
    answer = max(answer, (m-sum_budget) // (n-i) )
    sum_budget += budget[i]

print(min(answer, budget[-1]))