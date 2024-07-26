def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x = a + i * h
        sum += f(x)
    return h * sum

# Example usage
def f(x):
    return x**2  # Example function to integrate

a, b = 0, 1  # Integration limits
n = 1000  # Number of subintervals

result = trapezoidal_rule(f, a, b, n)
print(f"The approximate integral of x^2 from {a} to {b} is: {result:.6f}")