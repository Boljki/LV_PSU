import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

def non_func(x):
    y = 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) \
        - 1.1622*np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)
    return y

def add_noise(y):
    np.random.seed(14)
    varNoise = np.max(y) - np.min(y)
    y_noisy = y + 0.1*varNoise*np.random.normal(0,1,len(y))
    return y_noisy


x = np.linspace(1,10,50)
y_true = non_func(x)
y_measured = add_noise(y_true)

x = x[:, np.newaxis]
y_measured = y_measured[:, np.newaxis]


degrees = [2, 6, 15]


MSEtrain = []
MSEtest = []

plt.figure(figsize=(10,6))
plt.plot(x, y_true, 'k-', linewidth=2, label='Stvarna funkcija')

for d in degrees:
    
    poly = PolynomialFeatures(degree=d)
    x_poly = poly.fit_transform(x)
    
    
    np.random.seed(12)
    indeksi = np.random.permutation(len(x_poly))
    train_size = int(np.floor(0.7*len(x_poly)))
    indeksi_train = indeksi[:train_size]
    indeksi_test = indeksi[train_size:]
    
    xtrain = x_poly[indeksi_train, :]
    ytrain = y_measured[indeksi_train]
    xtest = x_poly[indeksi_test, :]
    ytest = y_measured[indeksi_test]
    
    
    model = LinearRegression()
    model.fit(xtrain, ytrain)
    
    
    ytrain_p = model.predict(xtrain)
    ytest_p = model.predict(xtest)
    
    MSEtrain.append(mean_squared_error(ytrain, ytrain_p))
    MSEtest.append(mean_squared_error(ytest, ytest_p))
    
    
    plt.plot(x, model.predict(x_poly), label=f'Model degree {d}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Usporedba modela s pozadinskom funkcijom')
plt.legend()
plt.show()


print("MSE na treningu:", MSEtrain)
print("MSE na testu:", MSEtest)