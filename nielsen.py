# X[] = { 1, 4, 7, 8, 10 }
# Y[] = { 2, 3, 9 }

# s = [1, 2, 3, 4, 7] # 5
# k = [8, 9, 10] # 3

# two array, sorted
# def sorted_arr(a, b):
    # x = [0] * len(a)
    # y = [0] * len(b)
    # print(x, y)
    



# x = [ 1, 4, 7, 8, 10 ]
# y = [2, 3, 9]

# sorted_arr(x, y)
























# Find a unique triplet in an array that sums up to 0.
# Input: 
nums = [-1,0,1,2,-1,-4]

def find_triplet(nums):
    target = 0
    result = []
    nums.sort() # [-4,-1,-1, 0,1,2]

    for i in range(len(nums)):
        # Skip the same `nums[i]` to avoid duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        l, r = i + 1, len(nums) - 1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum == target:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                # Skip the same `nums[l]` and `nums[r]` to avoid duplicates
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif sum < target:
                l += 1
            else:
                r -= 1

    return result


print(find_triplet(nums))




















# data = "Sikander Khan from Mumbai"
# # data = "two guys from Mumbai"

# # way - 2
# # def reverse_from(data):

    



# # way - 1
def reverse_from(data):
    result = []
    for word in data.split():
        if word.lower() == "from":
            result.append(word[::-1])
            continue
        result.append(word)
    return " ".join(result)

# print(reverse_from(data))
