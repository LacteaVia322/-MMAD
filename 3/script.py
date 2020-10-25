#вариант 8
import numpy as np
import matplotlib
import scipy.io
import matplotlib.pyplot as plt

def autocorrelate(a):
  n = len(a)
  cor = []
  for i in range(n//2, n//2+n):
    a1 = a[:i+1]   if i < n else a[i-n+1:]
    a2 = a[n-i-1:] if i < n else a[:2*n-i-1]
    cor.append(np.corrcoef(a1, a2)[0, 1])
  return np.array(cor)

a=10
print(a)
a=[1,2,3]
print(a)
a=[[1,2,3],[1,2,3],[1,2,3]]
print(a)
a=np.zeros((2,3))
print(a)
a=np.ones((2,3))
print(a)
a=np.random.randint(1,20,(2,3))
print(a)

array = np.loadtxt('test.txt')
print(array)

data = scipy.io.loadmat('./data/1D/var1.mat')
data.keys()
data = data['n']
dataMax=np.max(data) 
print(ma)
dataMin=np.min(data)
print(mi)
dataMedian=np.median(data)
print(med)
dataMean=np.mean(data)
print(mean)
dataVar=np.var(data)
print(var)
dataStd=np.std(data)
print(std)

plt.plot(data)
plt.show()
mean = np.mean(data) * np.ones(len(data))
var = np.var(data) * np.ones(len(data))
plt.plot(data, 'b-', mean, 'r-', mean-var, 'g--', mean+var, 'g--')
plt.grid()
plt.show()
plt.hist(data, bins=20)
plt.grid()
plt.show()

data = np.ravel(data)
cor = autocorrelate(data)
plt.plot(cor)
plt.show()

data = scipy.io.loadmat('./data/ND/var2.mat')
data.keys()
data=data['mn']

n = data.shape[1]
corr_matrix = np.zeros((n,n))
for i in range(0,n):
    for j in range(0,n):
        column1 = data[:,i]
        column2 = data[:,j]
        corr_matrix[i,j]=np.corrcoef(column1,column2)[0,1]
np.set_printoptions(precision=2)
print(corr_matrix)

plt.plot(data[:, 2], data[:, 5], 'b.')
plt.grid()
plt.show()


