import numpy as np
from sigmoid import sigmoid

def predict (X, Theta1, Theta2):
    a1=np.c_[np.ones(X.shape[0]), X]
    a2=sigmoid(np.dot(a1,Theta1.T))
    a3=np.c_[np.ones(a2.shape[0]), a2]
    h_x = sigmoid(np.dot(a3,Theta2.T))
    p = np.argmax(h_x, axis=1)+1
    return  p
