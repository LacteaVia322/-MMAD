# 3й вариант
# 2е задание
import random
import numpy as np
def sortString(a):
    return sorted(list(a))
b=sortString('this string needs to be sorted')
print("".join(b))

# 4е задание
def randomArrays(arrayQuantity, numbersQuantity):
    array=np.random.randint(0, 10, (arrayQuantity, numbersQuantity))
    print(array)
    max_idx, max_sum = 0, 0
    i=0
    while i<arrayQuantity:
        if sum(array[i]) > max_sum:
            max_sum = sum(array[i])
            max_idx = i
        i=i+1
    return array[max_idx]
x = randomArrays(3, 3)
print(x)
# 10е задание
def secondRandomArrays(arraySize):
    arr = np.random.sample(arraySize)
    values = (min(arr), max(arr))
    return values
values = secondRandomArrays(50)
maxValue = values[0]
minValue = values[1]
print(maxValue, minValue)

