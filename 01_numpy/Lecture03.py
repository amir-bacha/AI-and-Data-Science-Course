import numpy as np
array=np.array([1,2,3,4,5,6])
print(array)
print(np.sum(array)) # it adds all the values = 21
print(np.min(array)) # it returns the smallest value which is equal to 1
print(np.max(array)) # it returns the largest value whcih is equal to 6
print(np.average(array)) 
print(np.std(array))

marks=np.array([
    [60,70,55],
    [67,99,33],
    [90,58,80],
])
print(np.sum(marks,axis=1)) # it will add all the values along each rows 
print(np.mean(marks,axis=1))  # it will find mean
print(np.sum(marks,axis=0)) # it will add all the values along rows 
print(np.std(marks,axis=0)) # it will find std along vertically 

students=np.array([
    [85,90,78,88],
    [92,95,89,90],
    [67,89,44,66],
    [99,34,44,55],
    [91,77,54,33],
])
print(students)
names=np.array(['Ali','Sara','Ahmad','Aysha','Bilal'])
subjects=np.array( ['English','Programming','Statistics','Math'])
print(names)
print(subjects)
print(students.shape) # (5,4)
print(students.ndim) # 2
print(students.size)
print(students.dtype)
#  Ali programming marks
print('Ali programming marks are : ',students[0,1])
# All marks of Sara
print('All marks of Sara are : ', students[1, : ])
# Math Marks of every student
print('Math marks of every student : ',students[0: , 3: ])

# Adding 5 bonus marks to every student in every subject
bonus=5
students=students+bonus
print(students)
# Avarage marks in each subject
print('Avarage marks in each subject are : ', np.mean(students,axis=0))
# Highest marks in each subject
print(np.max(students,axis=0))
# Overall Standard deviation
print(np.std(students))
# Standard deviation in each subject
print(np.std(students, axis=0))






















