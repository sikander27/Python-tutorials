
"""
find longest subarray
diff between any element is not greater than k
sliding window min, max
- blend of two/3 diffrent
- neetcode -> le
# array -> [4, 6, 7, 7, 9]
window, minN, maxN, res
4 -- [4], [4], [4], [0, 0] = 0
6(1) -- [4, 6], [6], [4, 6], [0, 1] = 2
7(2) -- [4, 6, 7], [7], [6, 7], [1, 2 ] = 2
7(3) -- [4, 6, 7], [7], [6, 7], [0, 2 ] = 
[4, 6], 6, 4, [0, 1]
[4, 6, 7], 7, 4, [0, 1]
[6, 7], 7, 6, [1, 2]
[6, 7, 7], 7, 6, [1, 3]
[6, 7, 7, 9], 9, 6, [1, 3]
[7, 7, 9], 9, 7, [2, 4]
"""
# n * m
# 5, 7, 5
# arr = [1, 5,4 ,6, 8, 9, 10], k = 2
# sub_array = [1]
# l, r = 0, 1
# while l < r
# if doesn't : l  =r, r =r + 1
# 
from collections import deque


def longestSubArray(arr, k):
    max_q = deque()
    min_q = deque()
    res = [0, 0]
    max_len = l = 0

    for r in range(len(arr)):
        while max_q and arr[max_q[-1]] < arr[r]:
            max_q.pop()

        max_q.append(r)

        while min_q and arr[min_q[-1]] > arr[r]:
            min_q.pop()

        min_q.append(r)

        print(min_q, max_q, r)
        while arr[max_q[0]] - arr[min_q[0]] > k:
            l += 1
            if min_q[0] < l:
                min_q.popleft()
            if max_q[0] < l:
                max_q.popleft()
            print("updating", min_q, max_q, r, l)

        if (r - l + 1) > max_len:
            max_len = r - l + 1
            res = [l, r]
        print("---", r, l, res, min_q, max_q)
    l, r = res
    return arr[l:r+1]


arr = [4, 6, 7, 7, 9]
# arr = [1, 5,4 ,6, 8, 9, 10]
k = 2
print(longestSubArray(arr, 2))