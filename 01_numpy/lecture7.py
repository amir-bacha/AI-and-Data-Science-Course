import numpy as np
# #Concatenation : Adding arrays along an axisting axis
# student_a=np.array([
#     [1,2],
#     [3,4]
# ])
# student_b=np.array([
#     [5,6],
#     [7,8]
# ])
# print(student_a.shape)
# print(student_b.shape)
# result=np.concatenate((student_a,student_b), axis=0)
# stack_result=np.stack((student_a,student_b),axis=0)
# print(stack_result)
# print(stack_result.shape)

# a=np.array([
#     [1,2,3,4,],
#     [1,2,3,4,]
# ])

# b=np.array([
#     [7,8,9,10,11],
#     [7,8,9,10,11]
# ])
# concatenate=np.concatenate((a,b),axis=1)
# print(concatenate)
# print(concatenate.shape)
a=np.array([
    [1,2,3],
    [4,5,6]
])
b=np.array([
    [7,8,9],
    [10,11,12]
])
result=np.stack((a,b),axis=1)
print(result)

array=np.array([1,2,3,4,5,6,7])
result=np.array_split(array,2)
print(result)

twoD=np.array([
    [1,2,3,4],
    [5,6,7,8],
])
tResult=np.split(twoD,2,axis=1)
print(tResult)