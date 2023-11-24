import numpy as np
from scipy import integrate

def f1(x):
    return 1 / (0.5 * x + 1)

def f2(x):
    return x**2 * np.cos(x)

def f3(x):
    return 1 / np.sqrt(3 * x**2 + 1)

def simpsonMethod(func, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = func(x)
    h = (b - a) / n
    integral = h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    return integral

def rectangleMethod(func, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    integral = h * np.sum(y[:-1])
    return integral

def trapezoidalMethod(func, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    integral = h / 2 * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral

tolerance = 0.0001

result1Trapezoidal = integrate.quad(f1, 3.2, 4)[0]
result2Trapezoidal = integrate.quad(f2, 0.6, 1.4)[0]
result3Trapezoidal = integrate.quad(f3, 1.4, 2.2)[0]

result1Simpson = integrate.quad(f1, 3.2, 4)[0]
result2Simpson = integrate.quad(f2, 0.6, 1.4)[0]
result3Simpson = integrate.quad(f3, 1.4, 2.2)[0]

result1Rectangle = integrate.quad(f1, 3.2, 4)[0]
result2Rectangle = integrate.quad(f2, 0.6, 1.4)[0]
result3Rectangle = integrate.quad(f3, 1.4, 2.2)[0]

print(f"Метод прямокутників:")
print(f"Інтеграл 1: {rectangleMethod(f1, 3.2, 4, 10)} (Точне значення: {result1Rectangle})")
print(f"Інтеграл 2: {rectangleMethod(f2, 0.6, 1.4, 10)} (Точне значення: {result2Rectangle})")
print(f"Інтеграл 3: {rectangleMethod(f3, 1.4, 2.2, 10)} (Точне значення: {result3Rectangle})")

print(f"\nМетод Сімпсона:")
print(f"Інтеграл 1: {simpsonMethod(f1, 3.2, 4, 8)} (Точне значення: {result1Simpson})")
print(f"Інтеграл 2: {simpsonMethod(f2, 0.6, 1.4, 8)} (Точне значення: {result2Simpson})")
print(f"Інтеграл 3: {simpsonMethod(f3, 1.4, 2.2, 8)} (Точне значення: {result3Simpson})")

print(f"\nМетод трапецій:")
print(f"Інтеграл 1: {trapezoidalMethod(f1, 3.2, 4, 20)} (Точне значення: {result1Trapezoidal})")
print(f"Інтеграл 2: {trapezoidalMethod(f2, 0.6, 1.4, 20)} (Точне значення: {result2Trapezoidal})")
print(f"Інтеграл 3: {trapezoidalMethod(f3, 1.4, 2.2, 20)} (Точне значення: {result3Trapezoidal})")