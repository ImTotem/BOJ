n=int(input())
if n==1 or n==2 or n==4 or n==7:
    print(-1)
elif n % 5 == 2 or n%5==4:
    print ((n//5)+2)
elif n % 5 == 1 or n%5==3 :
    print ((n//5)+1)
else :
    print (n//5)