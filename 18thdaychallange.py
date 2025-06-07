# Heatmap plot in Python
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data= np.random.rand(10,12)
sns.heatmap(data,cmap="Reds")
plt.show()