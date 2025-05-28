# Pyramid pattern plot using python
import matplotlib.pyplot as plt
rows=5
plt.figure(figsize=(6,6))

for i in range(rows):
    for j in range(2*i+1):
        x=j-i
        y=-i
        plt.scatter(x,y, s=500, c='gold')
plt.xlim(-rows, rows)
plt.ylim(-rows, 1)


plt.axis('off')
plt.gca().set_aspect('equal', adjustable='datalim')
plt.title("Pyramid pattern plot", fontsize=14)

plt.show()