#The output would be a graph showing the original data points and the fitted polynomial curve.
import numpy as np
import matplotlib.pyplot as plt

# Define the data points
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([5.5, 43.1, 128, 290.7, 498.4, 978.67])

# Fit a 4th degree polynomial
p = np.polyfit(x, y, 4)

# Create a smoother set of x-values for the fitted curve
x2 = np.linspace(1, 6, 51)  # 51 points from 1 to 6

# Evaluate the fitted polynomial at the new x-values
y2 = np.polyval(p, x2)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Original data')  # Original points
plt.plot(x2, y2, '-', label='Polynomial fit')  # Fitted curve
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('4th Degree Polynomial Fit')
plt.legend()

# Show the plot
plt.show()

# Print the polynomial coefficients
print("Polynomial coefficients (highest degree first):")
print(p)