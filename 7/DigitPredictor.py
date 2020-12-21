import scipy.io as s_i
import predict as pr

def show(a):
    for row in a:
        for elem in row:
            print(elem, end=' ')
        print()
def __init__(self, t1, t2):
    self.Theta1 = t1
    self.Theta2 = t2
    
def predict(self):
    weights = s_i.loadmat('weights.mat')
    Theta1=weights['Theta1']
    Theta2=weights['Theta2']
    res=pr.predict(self, Theta1, Theta2)
    return res
    
