import numpy as np

def run():
    # 1) Умножение матриц A(3x5) и B(5x2)
    A = np.random.randint(1, 10, size=(3, 5))
    B = np.random.randint(1, 10, size=(5, 2))
    C = A @ B
    print("1) Умножение матриц A*B (3x5 * 5x2):")
    print("A:\n", A)
    print("B:\n", B)
    print("Результат:\n", C)
    print("-" * 50)

    # 2) Умножение матрицы (5x3) на трехмерный вектор
    M = np.random.randint(1, 10, size=(5, 3))
    v = np.random.randint(1, 10, size=(3,))
    result = M @ v
    print("2) Умножение матрицы M(5x3) на вектор v(3D):")
    print("M:\n", M)
    print("v:\n", v)
    print("Результат:\n", result)
    print("-" * 50)

    # 3) Решение системы линейных уравнений
    A_sys = np.random.randint(1, 10, size=(3, 3))
    b = np.random.randint(1, 10, size=(3,))
    x = np.linalg.solve(A_sys, b)
    print("3) Решение системы Ax = b:")
    print("A:\n", A_sys)
    print("b:\n", b)
    print("x:\n", x)
    print("Проверка A*x:\n", A_sys @ x)
    print("-" * 50)

    # 4) Определитель, обратная и транспонированная матрица
    A_det = np.random.randint(1, 10, size=(3, 3))
    det = np.linalg.det(A_det)
    inv = np.linalg.inv(A_det)
    trans = A_det.T
    print("4) Определитель, обратная и транспонированная матрица:")
    print("A:\n", A_det)
    print("Определитель:", det)
    print("Обратная A^-1:\n", inv)
    print("Транспонированная A^T:\n", trans)
    print("-" * 50)

    # 5) Проверка: det = произведение собственных значений (матрица 5x5)
    M5 = np.random.randint(1, 10, size=(5, 5))
    eigenvalues = np.linalg.eigvals(M5)
    det5 = np.linalg.det(M5)
    prod_eigen = np.prod(eigenvalues)
    print("5) Определитель vs произведение собственных значений (матрица 5x5):")
    print("M:\n", M5)
    print("Собственные значения:\n", eigenvalues)
    print("Определитель:", det5)
    print("Произведение собственных значений:", prod_eigen)
    print("-" * 50)


if __name__ == "__main__":
    run()