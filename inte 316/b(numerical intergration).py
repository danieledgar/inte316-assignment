import numpy as np

def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    return (b - a) / (2 * n) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def simpson_rule(f, a, b, n):
    if n % 2 != 0:
        n += 1
    x = np.linspace(a, b, n+1)
    y = f(x)
    return (b - a) / (3 * n) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]) + y[-1])

# Example usage
def f(x):
    return np.sin(x)

a, b = 0, np.pi
n = 100

print(f"Trapezoidal Rule: {trapezoidal_rule(f, a, b, n)}")
print(f"Simpson's Rule: {simpson_rule(f, a, b, n)}")
print(f"Actual value: {-np.cos(np.pi) + np.cos(0)}")