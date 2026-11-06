import numpy as np

class_a=np.array([
    [56,99,34,22],
    [45,88,32,19],
])
class_b=np.array([
    [23,90,89,56],
    [34,56,34,22],
])
# tO COMBINE ALL students
AllStudents=np.concatenate((class_a,class_b),axis=0)
print(AllStudents)
# Avarage of All students=
Mean=np.mean(AllStudents,axis=1)
print(Mean)








