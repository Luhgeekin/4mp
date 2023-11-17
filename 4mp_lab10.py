import numpy as np
import matplotlib.pyplot as plt


a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array([0.1 * val for val in a])
c = np.exp(-b) + b**2

t = np.vstack((a, b, c)).T
h = ["i", "xi", "f(xi)"]

print(f"{h[0]:<2} {h[1]:<5} {h[2]:<8}")
for r in t:
    print(f"{int(r[0]):<2} {r[1]:<5.2f} {round(r[2], 4):<8.4f}")

A_s = np.vstack([b, np.ones_like(b)]).T
m_s, c_s = np.linalg.lstsq(A_s, c, rcond=None)[0]

A_p = np.vstack([b**2, b, np.ones_like(b)]).T
a_p, b_p, c_p = np.linalg.lstsq(A_p, c, rcond=None)[0]

x_r = np.linspace(0, 1, 100)

y_s = m_s * x_r + c_s
y_p = a_p * x_r**2 + b_p * x_r + c_p

plt.scatter(b, c, label='Точки')
plt.plot(x_r, y_s, label=f'Пряма лінія: y = {m_s:.4f}x + {c_s:.4f}')
plt.plot(x_r, y_p, label=f'Парабола: y = {a_p:.4f}x^2 + {b_p:.4f}x + {c_p:.4f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()