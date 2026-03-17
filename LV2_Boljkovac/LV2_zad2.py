
import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),delimiter=",", skiprows=1)
mpg = data[:,0]
hp = data[:,3]
plt.scatter(mpg, hp)
plt.xlabel('mpg')
plt.ylabel('hp')
plt.title('Potrosnja automobila')
plt.show()


