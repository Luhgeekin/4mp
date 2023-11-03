import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

x = np.array([1.1, 1.4, 1.9, 2.5, 2.7])
y = np.array([2.91, 3.64, 4.55, 2.57, 0.24])

cs = CubicSpline(x, y, bc_type='natural')

xs = np.linspace(x.min(), x.max(), 100)
ys = cs(xs)

plt.figure()
plt.plot(x, y, 'o', label='Data points')
plt.plot(xs, ys, label='Cubic Spline')
plt.legend()
plt.xlabel('x')
plt.ylabel('Spline Value')
plt.title('Cubic Spline Interpolation')
plt.grid(True)
plt.show()