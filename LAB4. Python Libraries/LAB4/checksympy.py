import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def run():
    # ---------------- Символьные переменные ----------------
    x, y = sp.symbols('x y')

    # ---------------- Функция ----------------
    # выбираем, например, f(x) = x**3 + 2*x**2 - x + 1
    f = x**3 + 2*x**2 - x + 1
    print("Функция f(x):", f)

    # ---------------- Производная ----------------
    df = sp.diff(f, x)
    print("Производная f'(x):", df)

    # ---------------- Интеграл ----------------
    F = sp.integrate(f, x)
    print("Неопределенный интеграл ∫f(x)dx:", F)

    # ---------------- Графическое отображение ----------------
    x_vals = np.linspace(-5, 5, 400)
    f_lambd = sp.lambdify(x, f, 'numpy')
    df_lambd = sp.lambdify(x, df, 'numpy')
    F_lambd = sp.lambdify(x, F, 'numpy')

    plt.figure(figsize=(10,6))
    plt.plot(x_vals, f_lambd(x_vals), label='f(x)')
    plt.plot(x_vals, df_lambd(x_vals), label="f'(x)")
    plt.plot(x_vals, F_lambd(x_vals), label='∫f(x)dx')
    plt.legend()
    plt.title("Функция, её производная и интеграл")
    plt.grid(True)
    plt.show()

    # ---------------- Решение нелинейного уравнения ----------------
    # например, x**3 - x - 2 = 0
    eq = x**3 - x - 2
    sol = sp.solve(eq, x)
    print("Решение уравнения x^3 - x - 2 = 0:", sol)

    # ---------------- Решение системы нелинейных уравнений ----------------
    # пример: {x**2 + y**2 - 4 = 0, x*y - 1 = 0}
    eq1 = x**2 + y**2 - 4
    eq2 = x*y - 1
    sol_sys = sp.solve([eq1, eq2], (x, y))
    print("Решение системы {x^2 + y^2 = 4, x*y = 1}:", sol_sys)


if __name__ == "__main__":
    run()
