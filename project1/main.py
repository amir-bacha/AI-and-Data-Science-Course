import numpy as np
# Student performance prediction
# 5  Students study hours, attendence and assignment marks
students=np.array([
    [2,70,60],
    [3,80,75],
    [4,85,80],
    [5,90,85],
    [6,95,95]
])
normalized_data=students.astype(float)
normalized_data[:,0] =students[:,0] / 10
normalized_data[:,1] =students[:,1] / 100
normalized_data[:,2] =students[:,2] /100
print(normalized_data)
# Weight: weight represent the influence so we have three factors study 
#     hours, attendence and assignment so 
weights=np.array([
    [20],
    [30],
    [50],
])
print(weights)
# Now prediction
prediction=normalized_data @ weights
print('Prediction is : -----------')
print( prediction)
print(prediction.shape)
print(prediction.ndim)
passedStudent=[]
for i in prediction:
    if(i > 70):
        passedStudent.append(i)
        

print(passedStudent)