import pandas as pd
import numpy as np

mtcars = pd.read_csv('mtcars.csv')
br1 = (mtcars['am'] == 1).sum()
br2 = (mtcars['am'] == 0).sum()
print(br1)
print(br2)