import numpy as np
from scipy.misc import derivative


def f(x):
    return 4*pow(x, 4) + 4*pow(x,3) - 2*pow(x, 2)  - 3*x - 9 

eps = 0.001

def find_segments():
    search_range = np.arange(-10, 10, 1)
    
    a = None
    previous_x = None
    current_x  = None
    segments = []

    for x in search_range:
        x = round(x, 4)
        current_x = f(x)
        if previous_x != None and previous_x * current_x < 0:
            segments.append((a, x))
        a = x
        previous_x = current_x
    return segments



def newton_solver(a, b, eps):

    if f(b) * derivative(f, b, n=2) > 0:
        xi = b
    else:
        xi = a
    df = derivative(f, xi, n=1)
    xi_1 = xi - f(xi) / df

    while abs(xi_1 - xi) > eps:
        xi = xi_1
        xi_1 = xi - f(xi) / df

    return xi_1

def komb(a, b, eps):
    if derivative(f, a, n=1) * derivative(f, a, n=2) > 0:
        a0 = a
        b0 = b
    else:
        a0 = b
        b0 = a

    ai = a0
    bi = b0

    while abs(ai - bi) > eps:
        ai_1 = ai - f(ai) / derivative(f, ai, n=1)
        ai = ai_1

        bi_1 = bi - f(bi) / derivative(f, bi, n=1)
        bi = bi_1

    x = (ai_1 + bi_1) / 2

    return x

segments = find_segments()
for a, b in segments:
    N_solution = newton_solver(a, b, eps)
    K_solution = komb(a, b, eps)
    print(f"[{a}][{b}]")
    print('x =', N_solution,' - Newton\'s method')
    print('x =', K_solution,' - combined method ')