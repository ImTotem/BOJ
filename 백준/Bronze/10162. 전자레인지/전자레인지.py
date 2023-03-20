t=int(input())
print(f"{t//300} {t%300//60} {t%300%60//10}"if t%10==0 else-1)