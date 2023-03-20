from sys import stdin
input = stdin.readline

N = int(input())
tree = dict()

for _ in range(N):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

def preorder(root):
    ret = ''
    if root != '.':
        ret += root + preorder(tree[root][0]) + preorder(tree[root][1])

    return ret

def inorder(root):
    ret = ''
    if root != '.':
        ret += inorder(tree[root][0]) + root + inorder(tree[root][1])
    
    return ret

def postorder(root):
    ret = ''
    if root != '.':
        ret += postorder(tree[root][0]) + postorder(tree[root][1]) + root

    return ret

print(preorder('A'), inorder('A'), postorder('A'), sep="\n")