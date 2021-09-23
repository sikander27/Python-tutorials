
'''
Find max sum of 2 nums whose digits adds up to equal sum
'''

def sumofdigits(num):
    sum = 0
    while num>0:
        d = num % 10
        sum = sum + d
        num = num // 10
    return sum

def solution(A):
    max_sum = -1
    if len(A) <= 0:
        return max_sum
    reference = {}
    for i in A:
        sum = sumofdigits(i) # 6
        if sum in reference:
            cmax = i + reference[sum]
            if cmax > max_sum:
                max_sum = cmax
        else:
            reference[sum] = i
    return max_sum

a = [23,62, 52] #
print(solution(a))




