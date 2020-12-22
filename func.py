import numpy as np

# Third task
def compute_cost(X, y, theta):

    h_x = X * theta
    cost = np.sum(np.power(h_x - y, 2)) / (2 * X.shape[0])
    
    return cost

# Fourth task
def gradient_descent(X, y, alpha, iterations):
    
  m = X.shape[0]
  n = X.shape[1]
  theta = np.ones((n, 1))
  theta[0] = 0
  J_theta = np.zeros((iterations, 1))
  tmp = theta
  
  for i in range(iterations):
      J_theta[i] = compute_cost(X, y, theta)
      k = (alpha / m)
      s = np.zeros((n, 1))
      for j in range(0, n):
          s[j] = (np.multiply((X * tmp - y), X[:, j])).sum()
          tmp[j] = tmp[j] - k * s[j]
      theta = tmp        
  return tmp, J_theta

def predict(X, theta):
    return np.dot(X, theta)
