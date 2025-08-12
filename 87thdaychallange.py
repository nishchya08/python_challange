import numpy as np
# Filtering = Refers to the process of selecting elements from an array that matches a given condition

ages = np.array([[14,45,67,87,54,33,22],
                 [28,19,50,40,60,70,80]])

teenagers = ages[ages < 20]
#print(teenagers)
adults = ages[(ages >= 20) & (ages < 60)]
#print(adults)
seniors = ages[ages >=65]
#print(seniors)
evens = ages[ages % 2 == 0]
#print(evens)
odds = ages[ages % 2 != 0]
#print(odds)
adults = np.where(ages >= 20, ages, 0)
print(adults)

