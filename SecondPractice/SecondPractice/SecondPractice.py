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
    arraySum = np.sum(array, axis = 1)
    maxArg = np.argmax(arraySum)
    return array[maxArg]
x = randomArrays(3, 3)
print(x)
# 10е задание
def secondRandomArrays(arraySize):
    arr = np.random.sample(arraySize)
    return return min(arr), max(arr)

maxValue, minValue = secondRandomArrays(50)
print(maxValue, minValue)

