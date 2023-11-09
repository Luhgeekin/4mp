import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')
f = sp.exp(-2*x) + x**2

f_prime = sp.diff(f, x)
f_double_prime = sp.diff(f_prime, x)
f_triple_prime = sp.diff(f_double_prime, x)
x_value = 0

f_value = f.subs(x, x_value).evalf()
f_prime_value = f_prime.subs(x, x_value).evalf()
f_double_prime_value = f_double_prime.subs(x, x_value).evalf()
f_triple_prime_value = f_triple_prime.subs(x, x_value).evalf()

taylor_approximation = f_value + f_prime_value*(x - x_value) + (f_double_prime_value/2)*(x - x_value)**2 + (f_triple_prime_value/6)*(x - x_value)**3

print(f'Значення f({x}): {f}')
print(f'Значення першої похідної: {f_prime}')
print(f'Значення другої похідної: {f_double_prime}')
print(f'Значення третьої похідної: {f_triple_prime}')
print(f'Значення многочлена Тейлора: {taylor_approximation.evalf()}')

x_vals = np.linspace(-2, 2, 1000)
f_vals = np.array([f.subs(x, xi).evalf() for xi in x_vals])
taylor_vals = np.array([taylor_approximation.subs(x, xi).evalf() for xi in x_vals])

plt.figure(figsize=(8, 20))

plt.plot(x_vals, f_vals, label='f(x)')
plt.plot(x_vals, taylor_vals, label='Тейлорівське наближення')
plt.scatter([x_value], [f_value], color='red', marker='o', label='Точка оцінки')

plt.title('Графік функції та Тейлорівського наближення')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()