import math

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        f_x = f(x)
        df_x = df(x)

        if df_x == 0:
            print(f"Derivative zero at iteration {i}, method fails.")
            return None

        x_new = x - f_x / df_x

        if abs(f_x) < tol:
            return x_new

        x = x_new

    print("Newton-Raphson did not converge within the maximum number of iterations.")
    return None

def f(x):
    return x**4 - x - 10

def df(x):
    return 4*x**3 - 1 

root = newton_raphson(f, df, x0=2)

if root is not None:
    print(f"Root: {root}")
