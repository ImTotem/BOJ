from sys import stdin
input = stdin.readline

n, m = list(map(int, input().split()))
cards = sorted(list(map(int, input().split())))

def func():
    global n, m, cards

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                pick = cards[i]+cards[j]+cards[k]

                if pick > m:
                    break
                elif pick == m:
                    print(pick)
                    return
                else:
                    if m - pick < m - ans:
                        ans = pick
    
    print(ans)

func()