import numpy as np

#array1 = np.array([[1,2,3,4]])
#array2 = np.array([[1],[2], [3],[4]])
#print(array1.shape)
#print(array2.shape)
array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2= np.array([[1],[2], [3],[4],[5],[6],[7],[8],[9],[10]])
print(array1.shape)
print(array2.shape) 
print(array1 * array2)  # This will raise an error due to shape mismatch