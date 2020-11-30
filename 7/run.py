import scipy.io as s_i
import numpy as np
from displayData import displayData
from predict import predict
import matplotlib.pyplot as plt

#получаем матрицу и вектор-столбец
test_set = s_i.loadmat('test_set.mat')
weights = s_i.loadmat('weights.mat')
x_ts = test_set['X']
y_ts = np.int64(test_set['y'])
th1 = weights['Theta1']
th2 = weights['Theta2']

#получаем число строк в матрице
m = x_ts.shape[0]
#получаем массив индексов строк, перемешанных случайным образом
indexrow = np.random.permutation(m)
x = np.zeros((100, x_ts.shape[1]))
for i in range(100):
    x[i] = x_ts[indexrow[i]]
    
displayData(x)
#получаем результат предсказания нейросети
pre = predict(x_ts, th1, th2)
#сравниваем результаты предсказания сети с реальными значениями
y_ts.ravel()
q = (pre == y_ts.ravel())
#вывод результата массива сравнения
print(q)
res = np.mean(np.double(q))
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
mistake = np.where(pre != y_ts.ravel())[0]
qwerty = np.zeros((100,x_ts.shape[1]))
for i in range(100):
    qwerty[i] = x_ts[mistake[i]]
displayData(qwerty)
