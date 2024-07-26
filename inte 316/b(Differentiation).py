import numpy as np
import matplotlib.pyplot as plt

def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

# Example function
def f(x):
    return x**2 * np.sin(x)

# Calculate derivative
x = np.linspace(0, 2*np.pi, 100)
y = f(x)
dy_dx = numerical_derivative(f, x)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x)')
plt.plot(x, dy_dx, label="f'(x)")
plt.legend()
plt.title('Function and its Derivative')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()