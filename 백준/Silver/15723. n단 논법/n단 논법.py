import sys
input = lambda:sys.stdin.readline().strip()

def main():
    vec = [[False] * 26 for _ in range(26)]
    for i in range(26):
        vec[i][i] = True

    for _ in range(int(input())):
        l, r = map(lambda x:ord(x)-97, input().split(" is "))
        vec[l][r] = True
    
    for k in range(26):
        for i in range(26):
            for j in range(26):
                vec[i][j] |= vec[i][k] and vec[k][j]

    for _ in range(int(input())):
        l, r = map(lambda x:ord(x)-97, input().split(" is "))

        print(str(vec[l][r])[0])

main()