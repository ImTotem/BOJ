a,b,c=map(int,input().split())
d=int(input())
print((a+(b+((c+d)//60))//60)%24,(b+(c+d)//60)%60,(c+d)%60)