import sys
input = lambda:sys.stdin.readline().strip()

n, u, l = map(int, input().split())

def answer():
    if n < 1000: return "Bad"
    if 8000 <= u: return "Very Good"
    if 260 <= l: return "Very Good"
    return "Good"

print(answer())