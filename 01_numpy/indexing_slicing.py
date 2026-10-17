import numpy as np
fruits=np.array(["Banana", "apple", "mango", "orange"])
print(fruits[0]) # Banana
print(fruits[1]) # apple
print(fruits[2]) # mango
print(fruits[3]) # orange

# write a program to access all the element of array from start to end through indexes
for i in range(len(fruits)):
    print(fruits[i])
# Through negative indexing
for i in range(-1,-len(fruits),-1):
    print(fruits[i])


# Indexing of two dimensional array

matrix=np.array([[10,20,30],[40,50,60],[70,80,90],[100,110,120]])
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i,j],end=" ")
    print()

    