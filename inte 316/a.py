def f(x):
    return x**2 - x - 2

def regula_falsi(a, b, iterations):
    for i in range(iterations):
        fa = f(a)
        fb = f(b)
        x = (a * fb - b * fa) / (fb - fa)
        fx = f(x)
        
        print(f"Iteration {i+1}: x = {x:.6f}, f(x) = {fx:.6f}")
        
        if fx * fa < 0:
            b = x
        else:
            a = x
    
    return x

# Initial guesses
a, b = 1, 3

# Perform 3 iterations
result = regula_falsi(a, b, 3)
print(f"Final approximation: x = {result:.6f}") 