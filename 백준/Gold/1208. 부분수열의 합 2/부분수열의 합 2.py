from bisect import bisect_left as lower_bound, bisect_right as upper_bound
from itertools import combinations as comb
import sys

input = lambda: sys.stdin.readline().strip()

find_subsequence = lambda arr,target: upper_bound(arr, target) - lower_bound(arr, target)

get_subsequence = lambda arr:sorted(sum(j) for i in range(1, len(arr)+1) for j in comb(arr, i))

n, s = map(int, input().split())

sequence = list(map(int, input().split()))
left_arr = get_subsequence(sequence[:n//2])
right_arr = get_subsequence(sequence[n//2:])

answer = find_subsequence(left_arr, s) + find_subsequence(right_arr, s)
for i in left_arr:
    answer += find_subsequence(right_arr, s-i)

print(answer)