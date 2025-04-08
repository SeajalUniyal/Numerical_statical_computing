def gauss_elimination(a, b):
    n = len(b)

    # Forward elimination
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(a[k][i]) > abs(a[max_row][i]):
                max_row = k
        a[i], a[max_row] = a[max_row], a[i]
        b[i], b[max_row] = b[max_row], b[i]

        for k in range(i + 1, n):
            factor = a[k][i] / a[i][i]
            for j in range(i, n):
                a[k][j] -= factor * a[i][j]
            b[k] -= factor * b[i]

    # Back substitution
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        sum_ax = sum(a[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - sum_ax) / a[i][i]

    return x
# Solve the system:
# 2x + 3y + z = 1
# 4x + y - 2z = -2
# -2x + y + 2z = 7

a = [
    [2, 3, 1],
    [4, 1, -2],
    [-2, 1, 2]
]

b = [1, -2, 7]

solution = gauss_elimination(a, b)
print("Solution:", solution)
