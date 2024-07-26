import numpy as np

def newton_divided_difference(x, y):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])

    return coef[0]

def newton_interpolation(x, y):
    coef = newton_divided_difference(x, y)
    
    def P(x_val):
        n = len(x) - 1
        p = coef[n]
        for k in range(1, n+1):
            p = coef[n-k] + (x_val - x[n-k])*p
        return p
    
    return P

# Given data points
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Create the interpolating polynomial
P = newton_interpolation(x, y)

# Test the polynomial
x_test = np.linspace(1, 4, 100)
y_test = [P(xi) for xi in x_test]

# Plot the results
import matplotlib.pyplot as plt
plt.plot(x, y, 'ro', label='Data points')
plt.plot(x_test, y_test, label="Newton's polynomial")
plt.legend()
plt.grid(True)
plt.show()