# Creating the array in NumPy
import numpy as np
a=np.array([1, 2, 3, 4, 5])
print(a)
# Creating a 2D array in NumPy
b=np.array([[1, 2, 3], [4, 5, 6]])
print(b)
# Creating a 3D array in NumPy
c=np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(c)

# Some built-in functions in NumPy

# Creating an array of 0s and 1s
d=np.zeros(8)
e=np.ones((3,4))

f=np.full((3,4),4)
print(d)
print(e)
print (f)
