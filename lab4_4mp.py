import numpy as np

def task_1():
    #1. Знайти матрицю С = AB - BA
    a = np.array([[1, 2], [4, -1]])
    b = np.array([[2, -3], [-4, 1]])

    print(f"task 1\nC:\n{np.dot(a, b) - np.dot(b, a)}")

def task_2():
    #2. Піднести матриці до степеня
    a = np.array([[-1, 2], [0, 1]])
    power = 2

    print(f"task 2\nA^{power}:\n{np.linalg.matrix_power(a, power)}")

def task_3():
    #3. Знайти добуток матриць
    a = np.array([[3, 5], [2, 1]])
    b = np.array([[6, -1], [-3, 2]])

    print(f"task 3\nA*B:\n{np.dot(a, b)}")

def task_4():
    #4. Обчислити визначники
    a = np.array([[2, 3, 4], [1, 0, 6], [7, 8, 9]])

    print(f"task 4\n{np.linalg.det(a)}")

def task_5():
    #5. Обчислити визначники
    a = np.array([[1, 2, 3, 4], [-2, 1, -4, 3], [3, -4, -1, 2], [4, 3, -2, -1]])

    print(f"task 5\n{np.linalg.det(a)}")

def task_6():
    #6. Знайти обернену матрицю
    a = np.array([[1, 2, -3],[0, 1, 2],[0, 0, 1]])

    print(f"task 6\ninverse a:\n{np.linalg.inv(a)}")

def task_7():
    #7. Визначити ранг матриці
    a = np.array([[1, 2, 3, 4], [3, -1, 2, 5], [1, 2, 3, 4], [1, 3, 4, 5]])

    print(f"task 7\nrank: {np.linalg.matrix_rank(a)}")


def task_8():
    #8. Розв’язати систему лінійних рівнянь методом Крамера
    #17 варіант
    a = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])

    b = np.array([8, -11, -3])
    det_A = np.linalg.det(a)

    a1 = a.copy()
    a1[:, 0] = b
    det_A1 = np.linalg.det(a1)

    a2 = a.copy()
    a2[:, 1] = b
    det_A2 = np.linalg.det(a2)

    a3 = a.copy()
    a3[:, 2] = b
    det_A3 = np.linalg.det(a3)

    x1 = det_A1 / det_A
    x2 = det_A2 / det_A
    x3 = det_A3 / det_A

    print("Розв'язки методом Крамера:")
    print("x1 =", x1)
    print("x2 =", x2)
    print("x3 =", x3)

    x = np.linalg.solve(a, b)

    print("\nРозв'язки за матричним методом:")
    print("x =", x)


task_1()
task_2()
task_3()
task_4()
task_5()
task_6()
task_7()
task_8()