import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import approximate_taylor_polynomial

def g(x):
    return np.exp(-2*x) + x**2

x_vals = np.linspace(-2.0, 2.0, num=400)
plt.figure(figsize=(10, 6))
plt.plot(x_vals, g(x_vals), label="g(x) curve", color='blue')
degree = 3

taylor_g = approximate_taylor_polynomial(g, 0, degree, 1)
print('taylor_g=', taylor_g)

plt.plot(x_vals, taylor_g(x_vals), label=f"degree={degree}", color='red', linestyle='--')

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.0, shadow=True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Графік функції та наближення ,багаточленами Тейлора")
plt.tight_layout()
plt.grid()
plt.show()