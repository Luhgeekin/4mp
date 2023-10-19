import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange 

xi = np.array([-4, -2, 0, 3, -3.5, -3, -0.5, 2])
fi = np.array([-18, 8, -6, 3, None, None, None, None])

xi = xi[fi != None]
fi = fi[fi != None]

def lagrange_interpolation(x, xi, fi):
    n = len(xi)
    result = 0

    for i in range(n):
        term = fi[i]
        for j in range(n):
            if i != j:
                term *= (x - xi[j]) / (xi[i] - xi[j])
        result += term

    return result

x_values = [-1, 1, 2.5, -3]
y_values = [lagrange_interpolation(x, xi, fi) for x in x_values]


for x, y in zip(x_values, y_values):
    print(f'f({x}) ≈ {y:.3f}')


x_interp = np.linspace(min(xi), max(xi), 400)
y_interp = [lagrange_interpolation(x, xi, fi) for x in x_interp]

plt.plot(xi, fi, 'o', label='Задані точки')
plt.plot(x_interp, y_interp, label='Інтерполяційний багаточлен')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Графік інтерполяційної функції')
plt.grid()
plt.show()

f = lagrange(xi, fi)
fig = plt.figure(figsize=(7, 5))
plt.plot(x_interp, f(x_interp), 'b', xi, fi, 'ro')
plt.title('Lagrange Polynomial_2')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()


