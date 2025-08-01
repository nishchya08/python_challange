import numpy as np
array = np.array([[[1,2,3], ['A','B','C'], ['D','A','L']],
                 [[4,5,6], ['S','T','M'], ['S','W','Z']],
                 [[7,8,9], ['B','M','X'], ['S','K','P']]])
print(array.ndim)
print(array.shape)
word = array[0,2,1] + array[1,1,0] + array[2,2,0]
print(word)