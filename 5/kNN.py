import numpy as np
import math

# классификация методом k ближайших соседей
def k_nearest(X, k, obj):
    
#нормализация каждого столбца
 sub_X=X[:,0:-1]
 n=sub_X.shape[1]
 m=sub_X.shape[0]
 
 #рассчет евклидово расстояния от obj до каждого объекта sub_X
 distances= [dist(obj,item) for item in sub_X]

 #Получаем индексы соседей по мере их удаления от obj.
 index_dist=np.argsort(distances,axis=0)
 
 #выбор в отдельный вектор классы k ближайших соседей
 nearest_classes=[X[index_dist[item],2] for item in range(k)]
    
 # определяем наиболее часто встречающийся класс в этом векторе
 unique, counts = np.unique(nearest_classes, return_counts=True)
 object_class = unique[np.argmax(counts)]
 return object_class

# вычисление евклидова расстояния между двумя точками
def dist(p1, p2):
    return math.sqrt(sum((p1 - p2)**2))
