
import pandas as pd
import numpy as np


mtcars = pd.read_csv('mtcars.csv')
mtcars['masa_kg'] = mtcars['wt'] * 1000 * 0.453592
print('Masa auta u kg:')
print(mtcars[['car', 'masa_kg']].round(2))
