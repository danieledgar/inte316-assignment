import numpy as np

def power_iteration(A, num_iterations=1000, tolerance=1e-8):
    n = A.shape[0]
    v = np.random.rand(n)
    v = v / np.linalg.norm(v)
    
    for _ in range(num_iterations):
        Av = A.dot(v)
        v_new = Av / np.linalg.norm(Av)
        
        if np.allclose(v, v_new, atol=tolerance):
            break
        
        v = v_new
    
    eigenvalue = v.dot(A.dot(v)) / v.dot(v)
    return eigenvalue, v

# Given matrix
A = np.array([[4, 1, 1],
              [1, 3, -1],
              [1, -1, 2]])

eigenvalue, eigenvector = power_iteration(A)
print("Dominant Eigenvalue:", eigenvalue)
print("Corresponding Eigenvector:", eigenvector)