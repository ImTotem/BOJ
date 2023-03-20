h, m = list(map(int, input().split()))

if m >= 45: print(h, m-45)
else:
    if h-1 < 0:
        print(23, m-45+60)
    else:
        print(h-1, m-45+60)