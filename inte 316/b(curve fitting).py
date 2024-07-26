import numpy as np
import matplotlib.pyplot as plt

def polynomial_fit(x, y, degree):
    coeffs = np.polyfit(x, y, degree)
    p = np.poly1d(coeffs)
    return p

# Generate some noisy data
x = np.linspace(0, 10, 100)
y = 2 * x**2 - 5 * x + 3 + np.random.normal(0, 10, 100)

# Fit polynomials of different degrees
p2 = polynomial_fit(x, y, 2)
p5 = polynomial_fit(x, y, 5)

# Plot results
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Data')
plt.plot(x, p2(x), label='2nd degree fit')
plt.plot(x, p5(x), label='5th degree fit')
plt.legend()
plt.title('Polynomial Curve Fitting')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()