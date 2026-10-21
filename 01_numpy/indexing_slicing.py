# Create a two dimensional array. Slice it and reshape it into 1. 
import numpy as np
array=np.array([[1,2,3,4],[5,6,7,8]])
print(array)
print(array[0:2,1:3])
print(array.reshape([1,8]))