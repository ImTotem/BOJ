round = lambda n, d=0:(int((n:=int(n * 10**(d+1))/10)) + [0, 1][.4 < n-int(n)])/10**d

for i in range(int(input())):
    list_input = list(map(int, input().split(' ')))
    ave = sum(list_input[1:]) / list_input[0]
    count = 0
    for j in list_input[1:]:
        if j > ave:
            count += 1
    print(str('%.3f' % round(count / list_input[0] * 100, 3)) + '%')