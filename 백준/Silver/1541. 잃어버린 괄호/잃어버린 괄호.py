from sys import stdin
input = stdin.readline

n = input()

r=""
pre = -1
for i in range(len(n)):
    if n[i] == "-" or n[i] == "+" or i+1 == len(n):
        r+=n[pre+1:i].lstrip('0')+n[i]
        pre = i

braket = []

for i in range(len(r)):
    if r[i] == "-":
        if len(braket)%2!=0:
            braket.append(i)
        braket.append(i+1)

if len(braket)%2!=0:
    braket.append(len(r)-1)

braket.reverse()

for i in range(len(braket)):
    b="(" if i%2!=0 else ")"
    r = f"{r[:braket[i]]}{b}{r[braket[i]:]}"

print(eval(r))
