
import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),delimiter=",", skiprows=1)
mpg = data[:,0]
cyl = data[:,1]
mpg_6=[]
for i in range(len(data)):
    if cyl[i] == 6:
        mpg_6.append(mpg[i])

#mpg_6 = np.array(mpg_6)

print("Min:", mpg_6.min())
print("Max:", mpg_6.max())
print("Mean:", mpg_6.mean())