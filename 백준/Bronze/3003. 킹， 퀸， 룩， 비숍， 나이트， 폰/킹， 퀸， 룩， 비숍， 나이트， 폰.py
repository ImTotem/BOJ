n = list(map(int, input().split()))
print(*[[1, 1, 2, 2, 2, 8][i]-n[i] for i in range(len(n))])