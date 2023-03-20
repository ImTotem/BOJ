import sys

sys.setrecursionlimit(10**5)
input = lambda: sys.stdin.readline().strip()

n = int(input())
inorder, postorder = [list(map(int, input().split())) for _ in range(2)]

index = [0] * (n+1)
for i in range(n):
    index[inorder[i]] = i

ans = []

def preorder(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd:
        return

    root = postorder[postEnd]
    
    left = index[root] - inStart
    right = inEnd - index[root]

    ans.append(root)
    
    preorder(inStart, inStart+left-1, postStart, postStart+left-1)
    preorder(inEnd-right+1, inEnd, postEnd-right, postEnd-1)

preorder(0, n-1, 0, n-1)
print(*ans)