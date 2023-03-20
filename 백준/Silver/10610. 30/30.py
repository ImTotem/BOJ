n = sorted(list(map(int, list(input()))), reverse=True)

if n[len(n)-1]:
    print('-1')
else:
    if sum(n) % 3 != 0:
        print('-1')
    else:
        for i in n:
            print(i, end='')
