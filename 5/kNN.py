import numpy as np
import math

# классификация методом k ближайших соседей
def k_nearest(X, k, obj):
    
#нормализация каждого столбца
 sub_X=X[:,0:-1]
 n=len(sub_X[1,:])
 m=len(sub_X[:,1])
 distances=np.zeros(m)
 
 #рассчет евклидово расстояния от obj до каждого объекта sub_X
 for i in range(m):
    distances[i]=dist(obj,sub_X[i])
 #Получаем индексы соседей по мере их удаления от obj.
 index_dist=np.argsort(distances,axis=0)
 index_dist=np.argsort(index_dist,axis=0)

 min_1=list(index_dist).index(0)
 
 #выбор в отдельный вектор классы k ближайших соседей
 vektor=np.zeros(k)
 nearest_classes=np.zeros((k,2))
 for i in range(k):
   vektor[i]=list(index_dist).index(i)
 for i in range(k):
    nearest_classes[i]=X[int(vektor[i]),2]
 # определяем наиболее часто встречающийся класс в этом векторе
 unique, counts = np.unique(nearest_classes, return_counts=True)
 object_class = unique[np.argmax(counts)]
 return object_class

# вычисление евклидова расстояния между двумя точками
def dist(p1, p2):
    return math.sqrt(sum((p1 - p2)**2))
