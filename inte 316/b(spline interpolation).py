import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# Generate some data
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 2, 1, 3, 7, 10])

# Create cubic spline
cs = interpolate.CubicSpline(x, y)

# Generate points for smooth curve
xs = np.linspace(0, 5, 100)
ys = cs(xs)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Data points')
plt.plot(xs, ys, label='Cubic Spline')
plt.legend()
plt.title('Cubic Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

# Evaluate spline at a specific point
x_eval = 2.5
y_eval = cs(x_eval)
print(f"Value at x = {x_eval}: {y_eval}")