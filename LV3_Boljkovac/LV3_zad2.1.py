
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Učitavanje podataka
mtcars = pd.read_csv('mtcars.csv')

sns.barplot(x='cyl', y='mpg', data=mtcars, ci=None, palette='Set2') #ci uklanja prikaz intervala pouzdanovsti

# Naslovi i oznake
plt.title('Prosječna potrošnja automobila po broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Potrošnja (mpg)')

plt.show()