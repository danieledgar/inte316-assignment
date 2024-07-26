import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Simple Linear Regression
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])

model = LinearRegression()
model.fit(x, y)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue')
plt.plot(x, model.predict(x), color='red')
plt.title('Simple Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print(f"Simple Linear Regression: y = {model.intercept_:.2f} + {model.coef_[0]:.2f}x")

# Multiple Linear Regression
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3], [3, 3], [3, 4], [4, 4], [4, 5]])
Y = np.array([2, 3, 3, 4, 4, 5, 5, 6])

model = LinearRegression()
model.fit(X, Y)

print("\nMultiple Linear Regression:")
print(f"y = {model.intercept_:.2f} + {model.coef_[0]:.2f}x1 + {model.coef_[1]:.2f}x2")