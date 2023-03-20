a = input()
s = 0
for i in a:
    if i in "ABC":
        s += 3
    elif i in "DEF":
        s += 4
    elif i in "GHI":
        s += 5
    elif i in "JKL":
        s += 6
    elif i in "MNO":
        s += 7
    elif i in "PQRS":
        s += 8
    elif i in "TUV":
        s += 9
    elif i in r"WXYZX":
        s += 10
print(s)