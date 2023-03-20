from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**5)

in_ = []

while True:
    try:
        in_.append(int(input()))
    except:
        break

def postorder(nums):
    length = len(nums)
    
    if length < 2:
        return nums
    
    for i in range(1, length):
        if nums[i] > nums[0]:
            return postorder(nums[1:i]) + postorder(nums[i:]) + [nums[0]]
    
    return postorder(nums[1:]) + [nums[0]]

print(*postorder(in_), sep="\n")