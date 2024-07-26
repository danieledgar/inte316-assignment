import numpy as np

def qr_algorithm(A, num_iterations=1000, tolerance=1e-8):
    n = A.shape[0]
    Q = np.eye(n)
    
    for _ in range(num_iterations):
        Q_k, R_k = np.linalg.qr(A)
        A_new = R_k.dot(Q_k)
        
        if np.allclose(A, A_new, atol=tolerance):
            break
        
        A = A_new
        Q = Q.dot(Q_k)
    
    eigenvalues = np.diag(A)
    eigenvectors = Q
    
    return eigenvalues, eigenvectors

# Given matrix
A = np.array([[4, 1, 1],
              [1, 3, -1],
              [1, -1, 2]])

eigenvalues, eigenvectors = qr_algorithm(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:")
print(eigenvectors)