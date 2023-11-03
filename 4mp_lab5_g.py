import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)

equation1 = np.sin(Y - 1) + X - 1.3
equation2 = Y - np.sin(X + 1) - 0.8

plt.contour(X, Y, equation1, levels=[0], colors='r', label='sin(y - 1) + x = 1.3')
plt.contour(X, Y, equation2, levels=[0], colors='b', label='y - sin(x + 1) = 0.8')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.title('Графік рівнянь')
plt.show()