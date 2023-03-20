for i in range(int(input())):
    a = input()
    
    b = 0
    c = 0
    for j in range(len(a)):
        if a[j] == 'O':
            c += 1
            b += c
        else:
            c = 0
    print(b)