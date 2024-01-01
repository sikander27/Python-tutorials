# Given an array arr that represents a permutation of numbers from 1 to n.
# You have a binary string of size n that initially has all its bits set to zero. At each step i (assuming
# both the binary string and arr are 1-indexed) from 1 to n, the bit at position arr[i] is set to 1.
# You are also given an integer m. Find the latest step at which there exists a group of ones of length
# m. A group of ones is a contiguous substring of 1's such that it cannot be extended in either
# direction.
# Return the latest step at which there exists a group of ones of length exactly m. If no such group
# exists, return -1.

# Example 1:
# Input: arr = [3,5,1,2,4], m = 1
# Output: 4
# Explanation:
# Step 1: "00100", groups: ["1"]
# Step 2: "00101", groups: ["1", "1"]
# Step 3: "10101", groups: ["1", "1", "1"]
# Step 4: "11101", groups: ["111", "1"]
# Step 5: "11111", groups: ["11111"]
# The latest step at which there exists a group of size 1 is step 4.
# Example 2:
# Input: arr = [3,1,5,4,2], m = 2
# Output: -1
# Explanation:
# Step 1: "00100", groups: ["1"]
# Step 2: "10100", groups: ["1", "1"]
# Step 3: "10101", groups: ["1", "1", "1"]
# Step 4: "10111", groups: ["1", "111"]
# Step 5: "11111", groups: ["11111"]
# No group of size 2 exists during any step.

# Example 3:
# Input: arr = [2,1,3], m = 2
# Output: 2
# Example 4:
# Input: arr = [1], m = 1
# Output: 1

# Constraints:
# • n == arr.length
# • 1 <= m <= n <= 105
# • 1 <= arr[i] <= n
# • All integers in arr are distinct.

# [3,5,1,2,4]

def sk(bit_string, m):
    m_exist = False
    temp = ""
    for i in bit_string:
        if i == "1":
            temp = temp + i
            continue
        if temp != "":
            if temp == m * "1":
                m_exist = True
            temp = ""
    if temp == m * "1": # This was missing
        m_exist = True
    return m_exist


def get_groups(arr, m):
    bit_string = "0" * len(arr)
    latest_step = -1
    for step, index in enumerate(arr, 1):
        bit_string = bit_string[:index-1] + "1" + bit_string[index:]
        exists = sk(bit_string, m)
        if exists:
            latest_step = max(latest_step, step)
    return latest_step
# log(n2)



    # print(bit_string)

# print(get_groups([3,5,1,2,4], 1))
# print(get_groups([3,1,5,4,2], 2))
# print(get_groups([2,1,3], 2))
# print(get_groups([1], 1))
# print(sk("11101", 1))

def get_group(arr, m):
    bit_string = "0" * len(arr)
    latest_step = -1
    group_length = 0

    for step, index in enumerate(arr, 1):
        bit_string = bit_string[:index - 1] + "1" + bit_string[index:]

        if bit_string[index - 1] == "1":
            group_length += 1
        else:
            group_length = 1

        if group_length == m:
            latest_step = step

    return latest_step

print(get_group([3, 5, 1, 2, 4], 1))  # Output: 4
print(get_group([3, 1, 5, 4, 2], 2))  # Output: -1
print(get_group([2, 1, 3], 2))        # Output: 2
print(get_group([1], 1))  