import numpy as np
#Створіть прямокутну матрицю A, яка має N рядків і M стовпців з випадковими елементами. 
# Знайдіть найменший стовпчастий елемент матриці A, для якого сума абсолютних значень елементів максимальна.

n = 5  
m = 4  

a = np.random.rand(n, m)

column_sums = np.sum(np.abs(a), axis=0)
max_sum_column = np.argmax(column_sums)


print(f"A:\n{a}\nmax sum column: {max_sum_column}")