from sys import stdin
input = stdin.readline

while True:
    try:
        n = int(input())
        i = 1

        while True:
            if int('1'*i)%n == 0:
                print(i)
                break
            else:
                i+=1
    except:
        break