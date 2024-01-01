

# Given an unsorted array A of size N that contains only positive integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.
# In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.
# Note:- You have to return an ArrayList consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.


# Example 1:
# Input: N = 5, S = 12 A[] = {1,2,3,7,5}
# Sub = [] 
# 2 + 3 + 7 > 
# Output: [2 ,4 ]
# Explanation: The sum of elements from 2nd position to 4th position is 12.
# Example 2:
# Input: N = 10, S = 15 A[] = {1,2,3,4,5,6,7,8,9,10} 
# Output: 1 5
# Explanation: The sum of elements from 1st position to 5th position is 15.

def subArray(s, arr):
    "log(n*m)"
    l, r = 0, 0
    total_sum = 0
    while total_sum != s and r < len(arr) and l < len(arr):
        if total_sum < s:
            r += 1
        if total_sum > s:
            l += 1
        total_sum = sum(arr[l:r+1])
    return l + 1, r + 1


# def subArray(s, arr):
#     "log"
#     l, r = 0, 0
#     total_sum = 0
#     while total_sum != s and r < len(arr) and l < len(arr):
#         if total_sum < s:
#             r += 1
#         if total_sum > s:
#             l += 1
#         total_sum = sum(arr[l:r+1])
#     return l + 1, r + 1



print(subArray(12, [1,2,3,7,5]))
print(subArray(15, [1,2,3,4,5,6,7,8,9,10]))





