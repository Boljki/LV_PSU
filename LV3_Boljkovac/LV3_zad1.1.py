
import pandas as pd
import numpy as np


mtcars = pd.read_csv('mtcars.csv')
#potrosnja=mtcars.sort_values(by='mpg', ascending=False).head(5) #ascending - sortira od najeveceg prema najmanjem
#print(potrosnja['car'])
print(mtcars.tail(5))