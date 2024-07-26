import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x**2 + y**2 - x*y + x - y + 1

def gradient_f(x, y):
    df_dx = 2*x - y + 1
    df_dy = 2*y - x - 1
    return np.array([df_dx, df_dy])

def gradient_descent(learning_rate=0.1, num_iterations=1000, tolerance=1e-6):
    x, y = 0, 0  # Initial guess
    path = [(x, y)]
    
    for _ in range(num_iterations):
        grad = gradient_f(x, y)
        x_new = x - learning_rate * grad[0]
        y_new = y - learning_rate * grad[1]
        
        if np.abs(f(x_new, y_new) - f(x, y)) < tolerance:
            break
        
        x, y = x_new, y_new
        path.append((x, y))
    
    return x, y, path

# Run gradient descent
x_min, y_min, path = gradient_descent()

print(f"Minimum found at x={x_min:.4f}, y={y_min:.4f}")
print(f"Minimum value: {f(x_min, y_min):.4f}")

# Plotting
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.figure(figsize=(10, 8))
plt.contour(X, Y, Z, levels=50)
path = np.array(path)
plt.plot(path[:, 0], path[:, 1], 'ro-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gradient Descent Path')
plt.colorbar(label='f(x,y)')
plt.show()