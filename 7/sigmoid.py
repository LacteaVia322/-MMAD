import numpy as np

def sigmoid(z):
    g_z = 1 / (1 + np.exp(-z))
    return  g_z
