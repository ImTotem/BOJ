import sys
input = lambda:sys.stdin.readline().strip()

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.tree[self.n:] = arr[:]
        self.build()

    def build(self):
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def query(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l <= r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if not r & 1:
                res += self.tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res

    def update(self, idx, val):
        i = self.n + idx
        self.tree[i] = val
        while i >= 1:
            i >>= 1
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

def main():
    n, k, m = map(int, input().split())
    seg_tree = SegmentTree([int(input()) for _ in range(n)])

    ans = []
    for _ in range(k+m):
        a, b, c = map(int, input().split())
        if a == 1:
            seg_tree.update(b-1, c)
        else:
            ans.append(str(seg_tree.query(b-1, c-1)))
    
    return '\n'.join(ans)

if __name__ == "__main__":
    print(main())
