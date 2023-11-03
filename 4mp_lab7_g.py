import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([1.340, 1.345, 1.350, 1.355, 1.360, 1.365, 1.370, 1.375, 1.380, 1.385, 1.390])
y_data = np.array([4.2556, 4.3532, 4.4552, 4.5618, 4.6734, 4.7903, 4.9130, 5.0419, 5.1774, 5.3201, 5.4706])
x_interp = np.array([1.342, 1.346, 1.361, 1.381, 1.386, 1.394])

def newton_interpolation(x, x_data, y_data):
    n = len(x_data)
    f = y_data.copy()
    for i in range(1, n):
        f[0:n-i] = ((x - x_data[i:]) * f[0:n-i] - (x - x_data[:n-i]) * f[1:n-i+1]) / (x_data[0:n-i] - x_data[i:])
    return f[0]

y_interp = [newton_interpolation(x, x_data, y_data) for x in x_interp]

plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, label='Дані точки', color='red', marker='o')
plt.plot(x_interp, y_interp, label='Інтерполяція', color='blue', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Графік інтерполяційної функції')
plt.grid(True)
plt.show()