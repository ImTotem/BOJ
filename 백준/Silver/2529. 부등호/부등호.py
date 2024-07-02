import sys
input = lambda:sys.stdin.readline().strip()

def main():
    k = int(input())
    inequality = input().split()
    
    ans = []

    li = []
    def dfs():
        idx = len(li) - 1
        
        if len(li) == k+1:
            tmp = ''.join(map(str, li))
            ans.append(tmp)
            return

        for i in range(10):
            if i in li: continue

            if not li \
            or (inequality[idx] == '<' and li[idx] < i) \
            or (inequality[idx] == '>' and li[idx] > i):
                li.append(i)
                dfs()
                li.pop()

    dfs()
    
    return max(ans, key=int), min(ans, key=int)

print(*main(), sep="\n")