import numpy as np
import matplotlib.pyplot as plt
from func import compute_cost, gradient_descent, predict
from matplotlib import rc
font = {'family': 'Verdana', 'weight': 'normal'}
rc('font', **font)

# First task
data = np.matrix(np.loadtxt('ex1data1.txt', delimiter=','))
X = data[:, 0]
y = data[:, 1]
# Second task
plt.plot(X, y, 'g.')
plt.title('Зависимость прибыльности от численности')
plt.xlabel('Численность')
plt.ylabel('Прибыльность')
plt.show()

# Cost function
m = X.shape[0]
X_ones = np.c_[np.ones((m, 1)), X]
theta = np.matrix('[1; 2]')
print(compute_cost(X_ones, y, theta))

# Call method gradient_descent
theta, J_th = gradient_descent(X_ones, y, 0.02, 500)
print(theta)

# Cost change while gradient descent 
plt.plot(np.arange(500), J_th, 'k-')
plt.title('Снижение ошибки при градиентном спуске')
plt.xlabel('Итерация')
plt.ylabel('Ошибка')
plt.grid()
plt.show()

# Call method predict
test = np.ones((2,2))
test[0][1] = 2.72
test[1][1] = 3.14
test_prediction = predict(test, theta)
print(test_prediction)

# Sixth task
x = np.arange(min(X), max(X))
plt.plot(x, theta[1] * x.ravel() + theta[0], 'g--')
plt.plot(X, y, 'b.')
plt.grid()
plt.show()