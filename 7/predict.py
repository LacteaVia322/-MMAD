import numpy as np
from sigmoid import sigmoid

def predict (X, Theta1, Theta2):
    m=X.shape[0]
    ones=np.ones(m), X
    a1=np.c_[ones]
    z2=np.dot(a1,Theta1.T)
    a2=sigmoid(z2)
    z3=np.ones(a2.shape[0])
    a3=np.c_[z3, a2]
    h_x = sigmoid(np.dot(a3,Theta2.T))
    p = np.argmax(h_x, axis=1)+1
    return  p
