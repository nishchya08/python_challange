import numpy as np

#rng = np.random.default_rng()

#print(rng.integers(low=1, high=100, size=(3, 2)))
#print(np.random.uniform(low=-1, high=1, size=3))

rng = np.random.default_rng()
#array = np.array([1,2,3,4,5])
#np.random.shuffle(array)
#print(array)

fruits = np.array(['apple', 'banana', 'cherry', 'date'])
fruits = rng.choice(fruits, size =3, replace=False)
print(fruits)