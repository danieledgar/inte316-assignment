import numpy as np

def lagrange_interpolation(x, y):
    def L(i, x_val):
        n = len(x)
        result = 1.0
        for j in range(n):
            if j != i:
                result *= (x_val - x[j]) / (x[i] - x[j])
        return result
    
    def P(x_val):
        n = len(x)
        return sum(y[i] * L(i, x_val) for i in range(n))
    
    # Compute coefficients
    coeffs = np.polyfit(x, [P(xi) for xi in x], len(x)-1)
    return coeffs[::-1]  # Reverse to get ascending order of powers

# Example usage
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
coefficients = lagrange_interpolation(x, y)
print("Lagrange polynomial coefficients:", coefficients)