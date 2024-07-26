def f(x):
    return x**3 - 0.165*x**2 + 3.993e-4

def f_prime(x):
    return 3*x**2 - 0.33*x

def newton_method(x0, iterations):
    x = x0
    for i in range(iterations):
        fx = f(x)
        fpx = f_prime(x)
        x_new = x - fx / fpx
        error = abs((x_new - x) / x_new)
        
        print(f"Iteration {i+1}: x = {x_new:.6f}, f(x) = {f(x_new):.6f}, error = {error:.6f}")
        
        x = x_new
    
    return x

# Initial guess
x0 = 0.1

# Perform 3 iterations
result = newton_method(x0, 3)
print(f"Final approximation: x = {result:.6f}")