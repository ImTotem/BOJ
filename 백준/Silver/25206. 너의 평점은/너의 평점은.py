import sys
input = lambda:sys.stdin.readline().strip()

table = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

_sum = 0
sum_credit = 0

for i in range(20):
    subject, credit, grade = input().split()
    if grade != "P":
        credit, grade = float(credit), float(table[grade])
        _sum += credit * grade
        sum_credit += credit

print(_sum / sum_credit)