from statistics import mean
a = int(input())
n = list(map(int, input().split()))
print(mean(n)/max(n)*100)
