n, m, k = list(map(int, input().split()))

teamCount = 0

while n >= 2 and m >= 1 and n+m >= 3+k:
    n -=2
    m-=1
    teamCount+=1

print(teamCount)