import scipy.io as s_i
import numpy as np
from displayData import displayData
from predict import predict
import matplotlib.pyplot as plt

#---Доп задание---
class DigitPredictor:
    #метод предсказание для строки матрицы
    def predict(self, x):
        x= x.reshape((1, x.shape[0]))
        res=predict(x, self.Theta1,  self.Theta2)
        return res            
    #конструктор объкта класса, аргументы которого веса 
    def __init__(self, t1, t2):
        self.Theta1 = t1
        self.Theta2 = t2
    #метод для вывода изображения
    def show(self,x):
        x= x.reshape((1, x.shape[0]))
        displayData(x)  
        
#получаем матрицу и вектор-столбец
test_set = s_i.loadmat('test_set.mat')
weights = s_i.loadmat('weights.mat')
x_ts = test_set['X']
y_ts = np.int64(test_set['y'])
y_ts.ravel()
th1 = weights['Theta1']
th2 = weights['Theta2']

#----Доп задание----
#создание объекта класса, аргументы это веса
dg = DigitPredictor(th1,th2)
#вызов метода для вывода изображения строки матрицы
dg.show(x_ts[150])

#получаем число строк в матрице
m = x_ts.shape[0]
#получаем массив индексов строк, перемешанных случайным образом
indexrow = np.random.permutation(m)
x = np.zeros((100, x_ts.shape[1]))
for i in range(100):
    x[i]=np.random.choice(x_ts[i])
displayData(x)
#получаем результат предсказания нейросети
predicted = predict(x_ts, th1, th2)

#----Доп задание----
#вызов метода для предсказания строки матрицы
pr=dg.predict(x_ts[0])
res1 = np.mean(np.double(pr == y_ts.ravel()))
print(res1)

res = np.mean(np.double(predicted == y_ts.ravel()))
#выводим значение точности
print(res)
#выполнить предсказание для 5 случайных примеров из обучающей выборки
rp = np.random.permutation(m)
plt.figure()
for i in range(5):
     X2 = x_ts[rp[i],:]
     X2 = np.matrix(x_ts[rp[i]])
     
     pred = predict(X2.getA(), th1, th2)
     pred = np.squeeze(pred)
     pred_str = 'Neural Network Prediction: %d (digit %d)' % (pred, y_ts[rp[i]])
     displayData(X2, pred_str)
     
     plt.close()
#определяем индексы примеров, на которых нейросеть ошиблась     
mistake = np.where(predicted != y_ts.ravel())[0]
array_mistake = np.zeros((100,x_ts.shape[1]))
for i in range(100):
    array_mistake[i] = x_ts[mistake[i]]
displayData(array_mistake)


