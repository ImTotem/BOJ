d = list(map(int, input().split()))
d = sorted(d, key=d.count)[::-1]
print(10000+d[0]*1000 if d[0]==d[2]else 1000+d[0]*100 if len(set(d))==2 else max(d)*100)