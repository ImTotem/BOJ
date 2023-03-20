from sys import stdin
input = stdin.readline

mbti = ['ISTJ', 'ISTP', 'ISFJ', 'ISFP', 'INTJ', 'INTP', 'INFJ', 'INFP', 'ESTJ', 'ESTP', 'ESFJ', 'ESFP', 'ENTJ', 'ENTP', 'ENFJ', 'ENFP',
        'JTSI', 'PTSI', 'JFSI', 'PFSI', 'JTNI', 'PTNI', 'JFNI', 'PFNI', 'JTSE', 'PTSE', 'JFSE', 'PFSE', 'JTNE', 'PTNE', 'JFNE', 'PFNE']

n, m = map(int, input().split())
board = []

cnt = 0

for _ in range(n):
    line = input()
    board.append(line)
    for i in mbti:
        cnt += line.count(i)

for i in range(n-3):
    for j in range(m):
        mbt = board[i][j]+board[i+1][j]+board[i+2][j]+board[i+3][j]
        if mbt in mbti:
            cnt+=1
        
        if i + 3 <= n:
            if j + 3 <= m:
                mbt = board[i][j]+board[i+1][j+1]+board[i+2][j+2]+board[i+3][j+3]
                if mbt in mbti:
                    cnt += 1
            if j - 3 >= 0:
                mbt = board[i][j]+board[i+1][j-1]+board[i+2][j-2]+board[i+3][j-3]
                if mbt in mbti:
                    cnt += 1

print(cnt)