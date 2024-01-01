# for question see. codility-2.jpg

def solution(A):
    if len(A) <= 0:
        return 0
    reference = {}
    result = []
    for i in A:
        if i in reference:
            n = reference[i] + 1
            reference[i] = n
        else:
            reference[i] = 1
    for i,j in reference.items():
        if i == j:
            result.append(i)
    if len(result) == 0:
        return 0
    return max(result)

a = solution([3,3,2,2,5,5,5,5,5,4,3])
a = solution([])
print(a)