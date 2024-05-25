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
    hashmap = set()

    def register_nums(nums):
        print(nums)
        for i in nums:
            hashmap.add(i)

    nums.sort() # [-4,-1,-1, 0,1,2]
    # print(nums)
    for i in range(len(nums)):
        if nums[i] in hashmap:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            if nums[l] in hashmap:
                l += 1
            if nums[r] in hashmap:
                r -= 1
            sum = nums[i] + nums[l] + nums[r]
            if sum == target:
                register_nums([i, l, r])
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                break
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
# # def reverse_from(data):
# #     result = []
# #     for word in data.split():
# #         if word.lower() == "from":
# #             result.append(word[::-1])
# #             continue
# #         result.append(word)
# #     return " ".join(result)

# print(reverse_from(data))
