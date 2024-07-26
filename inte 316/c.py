import numpy as np

def linear_interpolation(x, x0, x1, y0, y1):
    return y0 + (x - x0) * (y1 - y0) / (x1 - x0)

# Given data
x = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

# Find the appropriate interval for x = 4.0
for i in range(len(x) - 1):
    if x[i] <= 4.0 <= x[i+1]:
        x0, x1 = x[i], x[i+1]
        y0, y1 = y[i], y[i+1]
        break

# Calculate y at x = 4.0
y_interpolated = linear_interpolation(4.0, x0, x1, y0, y1)

print(f"The interpolated y value at x = 4.0 is: {y_interpolated:.4f}")