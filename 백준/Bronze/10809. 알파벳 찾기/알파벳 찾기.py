S = input()
li = []
for i in range(26):
    if chr(97+i) in S:
        li.append(str(S.find(chr(97+i))))
    else:
        li.append('-1')

print( ' '.join(li) )