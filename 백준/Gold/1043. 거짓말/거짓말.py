from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
in_ = list(map(int, input().split()))

know_true_length = in_[0]
know_true = in_[1:] if know_true_length > 0 else []
parties = [set(list(map(int, input().split()))[1:]) for _ in range(M)]

# 과장된 이야기를 할 수 있는 파티의 수
if know_true_length == 0:
    print(M)
else:
    a = set(know_true)
    while True:
        flag = True

        for b in parties:
            c = a & b
            if c:
                a.update(b)
                parties.remove(b)
                M -= 1
                flag = False

        if flag:
            print(M)
            break