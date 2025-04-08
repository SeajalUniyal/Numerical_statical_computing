def jacobi(a, b, x0=None, tol=1e-6, max_iter=100):
    n = len(b)
    x = x0 or [0] * n 

    for itr in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            sum_ax = sum(a[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_ax) / a[i][i]

        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            print(f"Converged in {itr+1} iterations")
            return x_new

        x = x_new

    print("Jacobi method did not converge within the maximum number of iterations.")
    return x

# 10x + 2y + z = 9
# -3x - 6y + 2z = -16
# x + y + 5z = 15

a = [
    [10, 2, 1],
    [-3, -6, 2],
    [1, 1, 5]
]

b = [9, -16, 15]

initial_guess = [0, 0, 0]

solution = jacobi(a, b, x0=initial_guess)
print("Solution:", solution)
