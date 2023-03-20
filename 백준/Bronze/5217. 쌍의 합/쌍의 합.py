from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    
    pairs = []
    for i in range(n//2):
        if i+1 != n-i-1:
            pairs.append(f"{i+1} {n-i-1}")
    print(f"Pairs for {n}:", end=" ")
    print(*pairs, sep=", ")