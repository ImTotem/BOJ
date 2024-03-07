import sys
input = lambda:sys.stdin.readline().strip()

def is_wrong(arr):
    return True if len(set(arr)) != 9 else False

def main():
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    
    for i in range(9):
        if is_wrong(sudoku[i]) or\
            is_wrong(map(lambda x:x[i], sudoku)):
            return "INCORRECT"

    for k in range(3):
        for i in range(3):
            seg = []
            for j in range(3):
                seg.extend(sudoku[3*k+j][3*i:3*i+3:])
            if is_wrong(seg): return "INCORRECT"

    return "CORRECT"

for x in range(n:=int(input())):
    print(f"Case {x+1}: {main()}")
    if x+1 != n: input()