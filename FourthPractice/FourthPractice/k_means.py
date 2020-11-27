import numpy as np
import math

def dist(A, B):
  """
  Евклидово расстояние между двумя точками
  """
  if len(A) == len(B):
    r = math.sqrt(sum([(a_i - b_i)**2 for a_i, b_i in zip(A, B)]))
  return r

def class_of_each_point(X, centers):
  """
  Возвращает список индексов ближайших центров по каждой точке
  """
  m = len(X)
  k = len(centers)
  """
  Матрица расстояний от каждой точки до каждого центра
  """
  distances = np.zeros((m, k))
  for i in range(m):
    for j in range(k):
      distances[i, j] = dist(centers[j], X[i])
  """
  Поиск ближайшего центра для каждой точки
  """
  return np.argmin(distances, axis=1)

def curse(k,X):
    """
    Выполнение кластеризации алгоритмом k-means
    :param k: количество искомых кластерных центров
    :param Х: исходные данные (матрица объектов-признаков numpy.array)
    :return: координаты кластерных центров
    """
    m = X.shape[0]
    n = X.shape[1]

    curr_iteration = prev_iteration = np.zeros(m)
    centers = np.random.random((k, n))
    curr_iteration = class_of_each_point(X, centers)
    
    while True:
        if np.all(curr_iteration==prev_iteration):
            break;
        prev_iteration = curr_iteration
        """
        Вычисляем новые центры масс
        """
        for i in range(k):
            sub_X = X[curr_iteration == i, :]
            if len(sub_X) > 0:
                centers[i, :] = np.mean(sub_X, axis=0)
        """
        Приписываем каждую точку к заданному классу
        """
        curr_iteration = class_of_each_point(X, centers)       
    return centers

def kmeans(k, X):
    
  while True:
     centers = curse(k, X)
     if check(X, centers) == True:
         """
         Как только центры найдены правильно - выход из цикла,
         иначе снова запускается функция вычисления кластерных центров
         """ 
         break;
         
  return centers

def check(X, centers): 
    """
    Проверка кластерных центров
    :param X: исходные данные
    :param centers: кластерные центры, вычисленные функцией curse
    :return: True, если кластерные центры найдены правильно
             False, если кластерные центры найдены неправильно
    """                   
    minValue = np.min(X[:,1])
    maxValue = np.max(X[:,1])
    for i in range(centers.shape[0]):        
        for j in range(centers.shape[1]):            
            if (minValue > centers[i,j]) or (maxValue < centers[i,j]):
              """
              Если кластерные центры найдены неправильно, то функция возвращает false
              затем функция curse снова считает центры и отправляет их на проверку данной функцией
	            """ 
              return False     
    return True
