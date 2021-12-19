# def check(inp):
#     sttr = list(inp)
#     if (sorted(sttr)==sttr):
#         sttr[-2],sttr[-1] = sttr[-1],sttr[-2]
#         return(''.join(sttr))
#     else:
#         for i in range(len(sttr)):
#             if sttr[i] <= sttr[i+1]:
#                 i =+ 1
#             else:#acdb
#                 # if sttr[i+1]
#                 sttr[i-1], sttr[i] = sttr[i],sttr[i-1] #adcb
#                 left = sttr[:i]
#                 right = sttr[i:]
#                 right.sort()
#                 return left+right


# # sttr = 'acdb'
# sttr ='accde'
# temp = max(c,array)
# # 3 => 2(c) < 4(b)
# # acbdb
# print(check(sttr))
# # print(sorted(sttr)==list(sttr))
   
arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

for i in range(4):
    # for j in range(4):
    print(arr[i][i+1], end=' ')
    if i == 0 :
        i +1
    



#    [0][1] ...[0][3]
#    [1][3]...[3][3]     i +1 , j  
#    [3][2]..[3][0]     i, j-1
#    [2][0]..[1][0]     i  -1, j
#    [1][1]..[1][2]     i, j+1
#    [2][2]..[2][1]     j, i -1