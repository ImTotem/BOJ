from itertools import permutations as perm
import sys

input = lambda: sys.stdin.readline().strip()

nums = list(perm(map(str, range(1, 10)), 3))

for _ in range(int(input())):
    num, *sb = input().split()
    sb = list(map(int, sb))

    del_list = []

    for n in nums:
        s, b = 0, 0

        for j in range(3):
            if n[j] == num[j]:
                s += 1
            elif n[j] in num:
                b += 1
        
        if [s, b] != sb:
            del_list.append(n)
    
    for i in del_list:
        nums.remove(i)

print(len(nums))