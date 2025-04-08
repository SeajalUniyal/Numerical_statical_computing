import math

def secant_method(f, a, b, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        if f(b) - f(a) == 0:
            print("Division by zero error in iteration", i)
            return None

        x = b - (f(b) * (b - a)) / (f(b) - f(a))

        if abs(f(x)) < tol:
            return x
        a, b = b, x

    print("Secant method did not converge within the maximum number of iterations.")
    return None

def f(x):
    return x**4 - x - 10

root = secant_method(f, 1, 2)
if root is not None:
    print(f"Root: {root}")
