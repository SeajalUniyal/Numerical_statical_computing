def bisection_method(f, a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        print("Bisection fails. Function values at end points must have opposite signs")
        return None
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def f(x):
    return x**3 - x - 2


root = bisection_method(f, 1, 2)
if root is not None:
    print(f"Root: {root}")

  
