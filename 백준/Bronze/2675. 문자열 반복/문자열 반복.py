for i in range(int(input())):
    temp = input().split(' ')
    r = int(temp[0])
    s = temp[1]
    p = ""
    for j in s:
        p+=j*r
    print(p)