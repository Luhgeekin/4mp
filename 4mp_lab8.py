import numpy as np
from scipy.interpolate import CubicSpline

x = np.array([1.1, 1.4, 1.9, 2.5, 2.7])
y = np.array([2.91, 3.64, 4.55, 2.57, 0.24])

cs = CubicSpline(x, y)
splined_values = cs(x)

print("Значення сплайну у вузлових точках:")
for i in range(len(x)):
    print(f"C({x[i]}) = {splined_values[i]}, вихідна функція = {y[i]} ")

while True:
    x_val_input = input("Введіть точку x, для якої ви хочете обчислити значення (введіть 'q' для виходу): ")
    if x_val_input == 'q':
        break
    try:
        x_val = float(x_val_input)
        y_val = cs(x_val)
        print(f"f({x_val}) = {y_val}")
    except ValueError:
        print("Неправильний формат вводу.")