s = input().upper()
a_l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c_l = []

for i in a_l:
    c_l.append(s.count(i))

if c_l.count(max(c_l)) >= 2:
    print("?")
else:
    print(a_l[c_l.index(max(c_l))])
